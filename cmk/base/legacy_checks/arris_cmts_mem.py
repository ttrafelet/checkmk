#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


# mypy: disable-error-code="var-annotated"

from cmk.base.check_api import LegacyCheckDefinition
from cmk.base.check_legacy_includes.mem import check_memory_element
from cmk.base.config import check_info
from cmk.base.plugins.agent_based.agent_based_api.v1 import equals, OIDEnd, SNMPTree


def parse_arris_cmts_mem(string_table):
    parsed = {}
    for cid, heap, heap_free in string_table:
        # The Module numbers are starting with 0, not with 1 like the OIDs
        heap, heap_free = float(heap), float(heap_free)
        parsed.setdefault(
            int(cid) - 1,
            {
                "mem_used": heap - heap_free,
                "mem_total": heap,
            },
        )
    return parsed


def inventory_arris_cmts_mem(parsed):
    for k in parsed:
        yield k, {}


def check_arris_cmts_mem(item, params, parsed):
    if not (data := parsed.get(item)):
        return
    warn, crit = params.get("levels", (None, None))
    mode = "abs_used" if isinstance(warn, int) else "perc_used"
    yield check_memory_element(
        "Usage",
        data["mem_used"],
        data["mem_total"],
        (mode, (warn, crit)),
        metric_name="memused",
    )


check_info["arris_cmts_mem"] = LegacyCheckDefinition(
    detect=equals(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.4998.2.1"),
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.4998.1.1.5.3.2.1.1",
        oids=[OIDEnd(), "2", "3"],
    ),
    parse_function=parse_arris_cmts_mem,
    service_name="Memory Module %s",
    discovery_function=inventory_arris_cmts_mem,
    check_function=check_arris_cmts_mem,
    check_ruleset_name="memory_multiitem",
    check_default_parameters={
        "levels": (80.0, 90.0),
    },
)
