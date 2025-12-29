from amis import (
    Page,
    PageSchema,
    Html,
    Property,
    Service,
    Flex,
    ActionType,
    LevelEnum,
    Divider,
    Log,
    Alert,
    Form,
    Dialog,
    Select,
    Group,
    InputText,
    DisplayModeEnum,
    Horizontal,
)

from pagermaid.web.html import get_logo
from pagermaid.utils._config_utils import lang

logo = Html(html=get_logo())
select_log_num = Select(
    label=lang('web_log_count'),
    name="log_num",
    value=100,
    options=[
        {"label": 100, "value": 100},
        {"label": 200, "value": 200},
        {"label": 300, "value": 300},
        {"label": 400, "value": 400},
        {"label": 500, "value": 500},
    ],
)

log_page = Log(
    autoScroll=True,
    placeholder=lang('web_no_logs'),
    operation=["stop", "showLineNumber", "filter"],
    source={
        "method": "get",
        "url": "/pagermaid/api/log?num=${log_num | default:100}",
    },
)

cmd_input = Form(
    mode=DisplayModeEnum.horizontal,
    horizontal=Horizontal(left=0),
    wrapWithPanel=False,
    body=[
        InputText(
            name="command",
            required=True,
            clearable=True,
            addOn=ActionType.Dialog(
                label=lang('web_execute'),
                level=LevelEnum.primary,
                dialog=Dialog(
                    title=lang('web_execute_result'),
                    size="xl",
                    body=Log(
                        autoScroll=True,
                        placeholder=lang('web_execute_command'),
                        operation=["stop", "showLineNumber", "filter"],
                        source={
                            "method": "get",
                            "url": "/pagermaid/api/run_sh?cmd=${command | raw}",
                        },
                    ),
                ),
            ),
        )
    ],
)
eval_input = Form(
    mode=DisplayModeEnum.horizontal,
    horizontal=Horizontal(left=0),
    wrapWithPanel=False,
    body=[
        InputText(
            name="command",
            required=True,
            clearable=True,
            addOn=ActionType.Dialog(
                label=lang('web_execute'),
                level=LevelEnum.primary,
                dialog=Dialog(
                    title=lang('web_execute_result'),
                    size="xl",
                    body=Log(
                        autoScroll=True,
                        placeholder=lang('web_execute_command'),
                        operation=["stop", "showLineNumber", "filter"],
                        source={
                            "method": "get",
                            "url": "/pagermaid/api/run_eval?cmd=${command | raw}",
                        },
                    ),
                ),
            ),
        )
    ],
)

operation_button = Flex(
    justify="center",
    items=[
        ActionType.Ajax(
            label=lang('web_update'),
            api="/pagermaid/api/bot_update",
            confirmText=lang('web_reload_confirm'),
            level=LevelEnum.info,
        ),
        ActionType.Ajax(
            label=lang('web_restart_title'),
            className="m-l",
            api="/pagermaid/api/bot_restart",
            confirmText=lang('web_restart_confirm'),
            level=LevelEnum.danger,
        ),
        ActionType.Dialog(
            label=lang('web_logs'),
            className="m-l",
            level=LevelEnum.primary,
            dialog=Dialog(
                title=lang('web_logs'),
                size="xl",
                actions=[],
                body=[
                    Alert(
                        level=LevelEnum.info,
                        body=lang('web_log_refresh_tip'),
                    ),
                    Form(body=[Group(body=[select_log_num]), log_page]),
                ],
            ),
        ),
        ActionType.Dialog(
            label=lang('web_shell'),
            className="m-l",
            level=LevelEnum.warning,
            dialog=Dialog(title=lang('web_shell'), size="lg", actions=[], body=[cmd_input]),
        ),
        ActionType.Dialog(
            label=lang('web_eval'),
            className="m-l",
            level=LevelEnum.warning,
            dialog=Dialog(title=lang('web_eval'), size="lg", actions=[], body=[eval_input]),
        ),
    ],
)

status = Service(
    api="/pagermaid/api/status",
    body=Property(
        title=lang('web_status_info'),
        column=2,
        items=[
            Property.Item(label=lang('web_bot_version'), content="${version}"),
            Property.Item(label=lang('web_bot_uptime'), content="${run_time}"),
            Property.Item(label=lang('web_cpu_usage'), content="${cpu_percent}"),
            Property.Item(label=lang('web_ram_usage'), content="${ram_percent}"),
            Property.Item(label=lang('web_swap_usage'), content="${swap_percent}", span=2),
        ],
    ),
)

page_detail = Page(title="", body=[logo, operation_button, Divider(), status])
page = PageSchema(
    url="/home", label=lang('web_home'), icon="fa fa-home", isDefaultPage=True, schema=page_detail
)
