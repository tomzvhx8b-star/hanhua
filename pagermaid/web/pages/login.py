from amis import (
    Form,
    InputPassword,
    DisplayModeEnum,
    Horizontal,
    Remark,
    Html,
    Page,
    AmisAPI,
    Wrapper,
)

from pagermaid.web.html import get_logo
from pagermaid.utils._config_utils import lang

logo = Html(html=get_logo())
login_api = AmisAPI(
    url="/pagermaid/api/login",
    method="post",
    adaptor="""
        if (payload.status == 0) {
            localStorage.setItem("token", payload.data.token);
        }
        return payload;
    """,
)

login_form = Form(
    api=login_api,
    title="",
    body=[
        InputPassword(
            name="password",
            label=lang('web_password'),
            labelRemark=Remark(shape="circle", content=lang('web_login_password')),
        ),
    ],
    mode=DisplayModeEnum.horizontal,
    horizontal=Horizontal(left=3, right=9, offset=5),
    redirect="/admin",
)
body = Wrapper(className="w-2/5 mx-auto my-0 m:w-full", body=login_form)
login_page = Page(title="", body=[logo, body])
