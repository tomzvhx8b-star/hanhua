from amis import Form, InputSubForm, InputText, Static, Alert, PageSchema, Page

from pagermaid.utils._config_utils import lang

main_form = Form(
    title=lang('web_command_alias'),
    initApi="get:/pagermaid/api/command_alias",
    api="post:/pagermaid/api/command_alias",
    submitText=lang('web_save'),
    body=[
        InputSubForm(
            name="items",
            label=lang('web_command_alias_configured'),
            multiple=True,
            btnLabel="${alias} >> ${command}",
            draggable=True,
            addable=True,
            removable=True,
            addButtonText=lang('web_command_alias_add'),
            showErrorMsg=False,
            form=Form(
                title=lang('web_command_alias'),
                body=[
                    InputText(name="alias", label=lang('web_command_alias'), required=True),
                    InputText(name="command", label=lang('web_original_command'), required=True),
                ],
            ),
        )
    ],
)

test_form = Form(
    title=lang('web_test'),
    api="get:/pagermaid/api/test_command_alias?message=${message}",
    submitText=lang('web_test'),
    body=[
        InputText(name="message", label=lang('web_test_message_tip'), required=True),
        Static(
            className="text-red-600",
            name="new_msg",
            label=lang('web_command_alias_modified_message'),
            visibleOn="typeof data.new_msg !== 'undefined'",
        ),
    ],
)

tips = Alert(level="info")

page = PageSchema(
    url="/bot_config/command_alias",
    icon="fa fa-link",
    label=lang('web_command_alias'),
    schema=Page(title="", body=[tips, main_form, test_form]),
)
