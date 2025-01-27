#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# single
# <<<postfix_mailq_status:sep(58)>>>
# postfix/postfix-script: the Postfix mail system is running: PID: 2839
# postfix: Postfix is running with backwards-compatible default settings^M postfix: See http://www.postfix.org/COMPATIBILITY_README.html for details^M postfix: To disable backwards compatibility use "postconf compatibility_level=2" and "postfix reload"^M postfix/postfix-script: the Postfix mail system is running: PID: 3096

# multi instances
# <<<postfix_mailq_status:sep(58)>>>
# postfix/postfix-script: the Postfix mail system is running: PID: 12910
# postfix-external/postfix-script: the Postfix mail system is running: PID: 12982
# postfix-internal/postfix-script: the Postfix mail system is running: PID: 13051
# postfix-uat-cdi/postfix-script: the Postfix mail system is not running


# mypy: disable-error-code="var-annotated"

from cmk.base.check_api import LegacyCheckDefinition
from cmk.base.config import check_info


def parse_postfix_mailq_status(string_table):
    parsed = {}
    for line in string_table:
        stripped_line = [x.strip() for x in line]
        queuename = stripped_line[0].split("/")[0]
        if queuename == "postfix":
            queuename = ""
        parsed.setdefault(queuename, {})

        state_index = -1
        if len(stripped_line) > 2 and stripped_line[-2] == "PID":
            state_index = -3
            parsed[queuename]["pid"] = stripped_line[-1]
        parsed[queuename]["state"] = stripped_line[state_index]

    return parsed


def inventory_postfix_mailq_status(parsed):
    return [(queuename, None) for queuename in parsed]


def check_postfix_mailq_status(item, params, parsed):
    if item in parsed:
        state_readable = parsed[item]["state"]
        pid = parsed[item].get("pid")
        if state_readable.endswith("is running"):
            state = 0
        else:
            state = 2
        yield state, "Status: %s" % state_readable

        if pid:
            yield 0, "PID: %s" % pid


check_info["postfix_mailq_status"] = LegacyCheckDefinition(
    parse_function=parse_postfix_mailq_status,
    service_name="Postfix status %s",
    discovery_function=inventory_postfix_mailq_status,
    check_function=check_postfix_mailq_status,
)
