from fastapi import APIRouter
from fastapi.responses import JSONResponse

from pagermaid.web.api.utils import authentication
from pagermaid.common.update import update
from pagermaid.utils import lang

route = APIRouter()


@route.post("/bot_update", response_class=JSONResponse, dependencies=[authentication()])
async def bot_update():
    await update()
    return {"status": 0, "msg": lang('web_update_success')}


@route.post(
    "/bot_restart", response_class=JSONResponse, dependencies=[authentication()]
)
async def bot_restart():
    from pagermaid.web import web

    web.stop()
    return {}
