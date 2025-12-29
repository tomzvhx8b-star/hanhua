from amis import (
    InputText,
    Switch,
    Card,
    CardsCRUD,
    PageSchema,
    Page,
)

from pagermaid.utils._config_utils import lang

card = Card(
    header=Card.Header(
        title="$title",
        description="$id",
        avatarText="$title",
        avatarTextClassName="overflow-hidden",
    ),
    actions=[],
    toolbar=[
        Switch(
            name="enable",
            value="${status}",
            onText=lang('web_ignored'),
            offText=lang('web_not_ignored'),
            onEvent={
                "change": {
                    "actions": [
                        {
                            "actionType": "ajax",
                            "args": {
                                "api": {
                                    "url": "/pagermaid/api/set_ignore_group_status",
                                    "method": "post",
                                    "dataType": "json",
                                    "data": {
                                        "id": "${id}",
                                        "status": "${IF(event.data.value, 1, 0)}",
                                    },
                                },
                                "onSuccess": {
                                    "type": "tpl",
                                    "tpl": "${payload.msg}",
                                },
                                "onError": {
                                    "type": "tpl",
                                    "tpl": lang('web_operation_failed'),
                                },
                                "status": "${event.data.value}",
                                "id": "${id}",
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
    api="/pagermaid/api/get_ignore_group_list",
    loadDataOnce=True,
    source="${groups | filter:title:match:keywords_name}",
    filter={"body": [InputText(name="keywords_name", label=lang('web_group_name'))]},
    perPage=12,
    autoJumpToTopOnPagerChange=True,
    placeholder=lang('web_no_group_list'),
    footerToolbar=["switch-per-page", "pagination"],
    columnsCount=3,
    card=card,
)
page = PageSchema(
    url="/bot_config/ignore_groups",
    icon="fa fa-ban",
    label=lang('web_ignore_groups'),
    schema=Page(
        title=lang('web_ignore_groups'),
        subTitle=lang('web_ignore_group_tip'),
        body=cards_curd,
    ),
)
