from amis import InputText, Switch, Card, CardsCRUD, PageSchema, Page

from pagermaid.utils._config_utils import lang

card = Card(
    header=Card.Header(
        title="$name",
        description="$des",
        avatarText="$name",
        avatarTextClassName="overflow-hidden",
    ),
    actions=[],
    toolbar=[
        Switch(
            name="enable",
            value="${status}",
            onText=lang('web_plugin_enabled'),
            offText=lang('web_plugin_disabled'),
            onEvent={
                "change": {
                    "actions": [
                        {
                            "actionType": "ajax",
                            "args": {
                                "api": {
                                    "url": "/pagermaid/api/set_remote_plugin_status",
                                    "method": "post",
                                    "dataType": "json",
                                    "data": {
                                        "plugin": "${name}",
                                        "status": "${IF(event.data.value, 1, 0)}",
                                    },
                                },
                                "onSuccess": {
                                    "type": "tpl",
                                    "tpl": "${payload.msg}",  # 使用返回的 msg 字段作为成功消息
                                },
                                "onError": {
                                    "type": "tpl",
                                    "tpl": lang('web_operation_failed'),
                                },
                                "status": "${event.data.value}",
                                "plugin": "${name}",
                            },
                        },
                    ]
                }
            },
        )
    ],
)
cards_curd = CardsCRUD(
    mode="cards",
    title="",
    syncLocation=False,
    api="/pagermaid/api/get_remote_plugins",
    loadDataOnce=True,
    source="${rows | filter:name:match:keywords_name | filter:des:match:keywords_description}",
    filter={
        "body": [
            InputText(name="keywords_name", label=lang('web_plugin_name')),
            InputText(name="keywords_description", label=lang('web_plugin_description')),
        ]
    },
    perPage=12,
    autoJumpToTopOnPagerChange=True,
    placeholder=lang('web_plugin_no_info'),
    footerToolbar=["switch-per-page", "pagination"],
    columnsCount=3,
    card=card,
)
page = PageSchema(
    url="/plugins/remote",
    icon="fa fa-cloud-download",
    label=lang('web_plugin_repository'),
    schema=Page(title=lang('web_plugin_repository'), body=cards_curd),
)
