#!/usr/bin/env python3
# Copyright (C) 2023 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
import os

AGENT_OUTPUT_DIR = f"{os.path.dirname(__file__)}/agent_output"
SECTION_NAMES = [_ for _ in os.getenv("SECTION_NAMES", "").split(",") if _]
EXPECTED_OUTPUT_DIR = f"{os.path.dirname(__file__)}/check_output"
HOST_NAMES = [_ for _ in os.getenv("HOST_NAMES", "").split(",") if _]
CHECK_NAMES = [_ for _ in os.getenv("CHECK_NAMES", "").split(",") if _]

# API_SERVICES_COLS = ["state", "plugin_output", "check_command"]
API_SERVICES_COLS = [
    "accept_passive_checks",
    "acknowledged",
    "acknowledgement_type",
    "action_url",
    "action_url_expanded",
    "active_checks_enabled",
    "cache_interval",
    "cached_at",
    "check_command",
    "check_command_expanded",
    "check_flapping_recovery_notification",
    "check_freshness",
    "check_interval",
    "check_options",
    "check_period",
    "check_type",
    "checks_enabled",
    "comments",
    "comments_with_extra_info",
    "comments_with_info",
    "contact_groups",
    "contacts",
    "current_attempt",
    "current_notification_number",
    "custom_variable_names",
    "custom_variable_values",
    "custom_variables",
    "description",
    "display_name",
    "downtimes",
    "downtimes_with_extra_info",
    "downtimes_with_info",
    "event_handler",
    "event_handler_enabled",
    # "execution_time",
    "first_notification_delay",
    "flap_detection_enabled",
    # "flappiness",
    "groups",
    # "hard_state",
    "has_been_checked",
    "high_flap_threshold",
    "icon_image",
    "icon_image_alt",
    "icon_image_expanded",
    "in_check_period",
    "in_notification_period",
    "in_passive_check_period",
    "in_service_period",
    "initial_state",
    "is_executing",
    "is_flapping",
    "label_names",
    "label_source_names",
    "label_source_values",
    "label_sources",
    "label_values",
    "labels",
    # "last_check",
    # "last_hard_state",
    # "last_hard_state_change",
    # "last_notification",
    # "last_state",
    # "last_state_change",
    # "last_time_critical",
    # "last_time_ok",
    # "last_time_unknown",
    # "last_time_warning",
    # "latency",
    # "long_plugin_output",
    "low_flap_threshold",
    "max_check_attempts",
    "metrics",
    # "modified_attributes",
    # "modified_attributes_list",
    # "next_check",
    # "next_notification",
    "no_more_notifications",
    "notes",
    "notes_expanded",
    "notes_url",
    "notes_url_expanded",
    "notification_interval",
    "notification_period",
    "notification_postponement_reason",
    "notifications_enabled",
    "obsess_over_service",
    "passive_check_period",
    "pending_flex_downtime",
    "percent_state_change",
    # "perf_data",
    "plugin_output",
    "pnpgraph_present",
    # "previous_hard_state",
    "process_performance_data",
    "retry_interval",
    # "robotmk_last_error_log",
    # "robotmk_last_error_log_gz",
    # "robotmk_last_log",
    # "robotmk_last_log_gz",
    "scheduled_downtime_depth",
    "service_period",
    # "staleness",
    "state",
    "state_type",
    "tag_names",
    "tag_values",
    "tags",
]
