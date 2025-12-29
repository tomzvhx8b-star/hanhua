import sys

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pyrogram.errors import BadRequest, AuthTokenExpired
from pyrogram.raw.functions.account import InitTakeoutSession
from pyrogram.raw.functions.updates import GetState
from starlette.responses import HTMLResponse

from pagermaid.common.reload import load_all
from pagermaid.services import bot
from pagermaid.utils import lang, logs
from pagermaid.web.api import authentication
from pagermaid.web.html import get_web_login_html
from pyromod.methods.sign_in_qrcode import authorize_by_qrcode_web
from pyromod.utils.errors import QRCodeWebCodeError, QRCodeWebNeedPWDError


class UserModel(BaseModel):
    password: str


class WebLogin:
    def __init__(self):
        self.is_authorized = False
        self.need_password = False
        self.password_hint = ""

    async def connect(self):
        if not bot.is_connected:
            self.is_authorized = await bot.connect()

    @staticmethod
    async def initialize():
        if bot.is_connected and not bot.is_initialized:
            await bot.initialize()

    @staticmethod
    def has_login():
        return bot.me is not None

    @staticmethod
    async def init_bot():
        logs.info(f"{lang('save_id')} {bot.me.first_name}({bot.me.id})")
        await load_all()
        logs.info(lang("start"))

    async def init(self):
        await self.connect()
        if not self.is_authorized:
            return
        if not await bot.storage.is_bot() and bot.takeout:
            bot.takeout_id = (await bot.invoke(InitTakeoutSession())).id

        await bot.invoke(GetState())
        bot.me = await bot.get_me()
        if bot.me.is_bot:
            sys.exit(0)
        await self.initialize()
        await self.init_bot()


route = APIRouter()
html_route = APIRouter()
web_login = WebLogin()
web_login_html = get_web_login_html()


@route.get("/web_login", response_class=JSONResponse, dependencies=[authentication()])
async def web_login_qrcode():
    if web_login.has_login():
        return {"status": 0, "msg": lang('web_login_logged')}
    try:
        await web_login.connect()
        if not web_login.is_authorized:
            await authorize_by_qrcode_web(bot)
            web_login.is_authorized = True
        await web_login.init()
        return {"status": 0, "msg": lang('web_login_success')}
    except QRCodeWebCodeError as e:
        web_login.need_password = False
        return {"status": 1, "msg": lang('web_login_no_qrcode'), "content": e.code}
    except QRCodeWebNeedPWDError as e:
        web_login.need_password = True
        web_login.password_hint = e.hint or ""
        return {"status": 2, "msg": lang('web_login_need_password'), "content": web_login.password_hint}
    except AuthTokenExpired:
        return {"status": 3, "msg": lang('web_login_expired')}
    except BadRequest as e:
        return {"status": 3, "msg": e.MESSAGE}
    except Exception as e:
        return {"status": 3, "msg": f"{type(e)}"}


@route.post("/web_login", response_class=JSONResponse, dependencies=[authentication()])
async def web_login_password(user: UserModel):
    if web_login.has_login():
        return {"status": 0, "msg": lang('web_login_logged')}
    if not web_login.need_password:
        return {"status": 0, "msg": lang('web_login_no_password_needed')}
    try:
        await authorize_by_qrcode_web(bot, user.password)
        web_login.is_authorized = True
        await web_login.init()
        return {"status": 0, "msg": lang('web_login_success')}
    except QRCodeWebCodeError as e:
        return {"status": 1, "msg": lang('web_login_relogin'), "content": e.code}
    except QRCodeWebNeedPWDError as e:
        web_login.need_password = True
        return {"status": 2, "msg": lang('web_login_wrong_password'), "content": e.hint or ""}
    except AuthTokenExpired:
        web_login.need_password = False
        return {"status": 3, "msg": lang('web_login_expired')}
    except BadRequest as e:
        return {"status": 3, "msg": e.MESSAGE}
    except Exception as e:
        return {"status": 3, "msg": f"{type(e)}"}


@html_route.get("/web_login", response_class=HTMLResponse)
async def get_web_login():
    return web_login_html
