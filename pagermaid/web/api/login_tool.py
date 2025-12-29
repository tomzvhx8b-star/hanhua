import os
from pyrogram import Client

# 1. 填入你刚才获取的 API_ID 和 API_HASH
api_id = 31882755
api_hash = "bc6c24b6208f18df94232e2a6d7fc44d"

print("正在启动登录工具...")

# 2. 创建一个名为 pagermaid 的客户端
# 它会在当前目录下生成 pagermaid.session 文件
with Client("pagermaid", api_id=api_id, api_hash=api_hash) as app:
    print("\n登录成功！")
    print("你的 session 文件已经生成在文件夹里了。")
    # 导出一串字符作为备用（如果以后不想传文件，可以用这个字符串）
    print("\n这是你的 STRING_SESSION (建议保存到记事本):")
    print(app.export_session_string())