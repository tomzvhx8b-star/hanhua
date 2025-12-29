from fastapi import APIRouter
from fastapi.responses import JSONResponse

from pagermaid.common.alias import AliasManager
from pagermaid.web.api.utils import authentication
from pagermaid.utils._config_utils import lang

route = APIRouter()


@route.get(
    "/command_alias", response_class=JSONResponse, dependencies=[authentication()]
)
async def get_command_alias():
    alias = AliasManager()
    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": alias.get_all_alias_dict(),
        },
    }


@route.post(
    "/command_alias", response_class=JSONResponse, dependencies=[authentication()]
)
async def add_command_alias(data: dict):
    data = data["items"]
    try:
        await AliasManager.save_from_web(data)
        return {"status": 0, "msg": lang('web_command_alias_save_success')}
    except Exception:
        return {"status": 1, "msg": lang('web_command_alias_save_failed')}


@route.get(
    "/test_command_alias", response_class=JSONResponse, dependencies=[authentication()]
)
async def test_command_alias(message: str):
    alias = AliasManager()
    return {
        "status": 0,
        "msg": lang('web_test_success'),
        "data": {
            "new_msg": alias.test_alias(message),
        },
    }
