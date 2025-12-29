# PagerMaid-Pyro 深度汉化版

<p align="center">
  <img src="https://img.shields.io/badge/PagerMaid-Pyro-深度汉化版-blue?style=for-the-badge" alt="PagerMaid-Pyro Chinese Version">
  <img src="https://img.shields.io/badge/Telegram-飞机Bot-orange?style=for-the-badge" alt="Telegram Bot">
  <img src="https://img.shields.io/badge/支持-Windows%20%7C%20Linux%20%7C%20macOS-green?style=for-the-badge" alt="Platform Support">
</p>

---

## 📖 项目简介

PagerMaid-Pyro 深度汉化版是一个专为「飞机」（Telegram）设计的汉化 Bot 项目。本项目在原版基础上进行了完整的本地化适配，让中文用户能够更方便地使用这款强大的 Telegram 管理 Bot。

### 🌟 本版特点

- **全中文界面**：所有消息提示均为中文
- **中文命令提示**：命令帮助文档已翻译
- **Web 管理界面汉化**：浏览器管理界面已全面汉化
- **详细安装文档**：配套完整的中文安装指南
- **一键汉化脚本**：支持自动化部署

---

## 🚀 快速开始

如果您是第一次使用，请按照以下步骤完成安装。整过程大约需要 10 到 15 分钟。

### 第一步：准备环境

请确保您的电脑上已经安装了以下软件：

| 软件 | 说明 | 获取方式 |
|------|------|----------|
| Python 3.10 或更高版本 | 编程语言环境 | 访问 python.org 下载 |
| Git | 版本控制工具 | 访问 git-scm.com 下载 |
| Telegram 账号 | 需要能接收短信的手机号 | 手机应用商店下载 |

**检查 Python 是否已安装：**

打开终端（Windows 用户按 `Win + R`，输入 `cmd`，回车），输入：

```bash
python --version
```

如果显示类似 `Python 3.10.12`，说明已安装。如果没有，请先安装 Python。

### 第二步：下载项目

在终端中执行以下命令：

```bash
# 克隆项目到本地
git clone https://github.com/您的用户名/PagerMaid-Pyro.git

# 进入项目目录
cd PagerMaid-Pyro
```

### 第三步：安装依赖

执行以下命令安装项目所需的依赖：

```bash
pip install -r requirements.txt
```

> 💡 **小提示**：如果安装速度慢或失败，可以尝试使用国内镜像源：
> ```bash
> pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
> ```

### 第四步：获取 API 凭证

**这是最重要的一步！** Telegram 要求每个 Bot 都需要 API 凭证才能使用。

#### 4.1 访问 Telegram 开发者页面

1. 用浏览器打开：https://my.telegram.org/apps
2. 输入您的手机号码并点击「Next」
3. 您会收到一条验证码短信，输入验证码完成登录

#### 4.2 创建应用

1. 点击页面上的「Create New Application」按钮
2. 填写以下信息（都可以随便填）：
   - **App title**：填「MyPagerMaid」
   - **Short name**：填「pagermaid」
   - **Platform**：选择「Other」
   - **Description**：简单描述一下，比如「My Telegram Bot」

#### 4.3 获取凭证

创建成功后，页面会显示您的 API 凭证：

```
App api_id: 1234567        # 记下来，这是数字
App api_hash: abcdef1234567890abcdef1234567890  # 记下来，这是字符串
```

> ⚠️ **重要提示**：
> - `api_id` 是纯数字，不要加引号
> - `api_hash` 是一串字母和数字
> - 请保管好这些凭证，不要分享给别人

### 第五步：配置项目

现在把刚才获取的 API 凭证填入配置文件。

1. 用文本编辑器打开 `data/config.yml` 文件
2. 找到以下两行：

```yaml
api_id: "ID_HERE"
api_hash: "HASH_HERE"
```

3. 将 `ID_HERE` 替换为您的 `api_id`（纯数字）
4. 将 `HASH_HERE` 替换为您的 `api_hash`

修改后应该是这样的（以 1234567 为例）：

```yaml
api_id: "1234567"
api_hash: "abcdef1234567890abcdef1234567890"
```

### 第六步：运行汉化脚本（可选）

如果您下载的是带有一键汉化脚本的版本，可以执行：

```bash
python install_zh.py
```

这个脚本会自动完成以下操作：

- ✅ 安装中文语言文件
- ✅ 应用模块汉化
- ✅ 配置默认语言为中文
- ✅ 自动备份原文件（如果需要回退）

### 第七步：启动 Bot

一切准备就绪，现在可以启动 Bot 了！

在终端中执行：

```bash
python -m pagermaid
```

首次启动时会发生以下情况：

1. **如果启用了二维码登录**：屏幕上会显示一个二维码，打开 Telegram 扫描即可登录
2. **如果启用了 Web 登录**：打开浏览器访问 `http://127.0.0.1:3333`，输入密码登录

登录成功后，Bot 会自动初始化。稍等片刻，当您看到类似「PagerMaid-Pyro 已启动」的提示时，就可以开始使用了！

---

## 📖 使用指南

### 基本命令

Bot 启动后，在 Telegram 中向它发送以下命令即可使用：

| 命令 | 功能说明 | 使用方法 |
|------|----------|----------|
| `-ping` | 测试 Bot 是否在线 | 直接发送 `-ping` |
| `-help` | 查看所有命令 | 直接发送 `-help` |
| `-id` | 获取当前聊天的 ID | 直接发送 `-id` |
| `-ver` | 查看 Bot 版本信息 | 直接发送 `-ver` |
| `-restart` | 重启 Bot | 直接发送 `-restart` |
| `-update` | 更新 Bot 到最新版本 | 直接发送 `-update` |

### Web 管理界面

PagerMaid-Pyro 提供了可视化的 Web 管理界面，您可以通过浏览器进行更多操作。

**访问地址**：`http://127.0.0.1:3333`

**主要功能**：

| 功能 | 说明 |
|------|------|
| 状态监控 | 查看 Bot 运行状态、CPU、内存使用情况 |
| 日志查看 | 实时查看 Bot 运行日志 |
| 命令执行 | 在浏览器中执行 Shell 命令 |
| 插件管理 | 安装、卸载、启用、禁用插件 |
| 群组设置 | 管理忽略群组、命令别名等 |

---

## ❓ 常见问题

### 问题一：提示「API_ID or API_HASH is invalid」

**原因**：配置文件填写错误。

**解决方法**：
1. 确认 `api_id` 是纯数字，没有多余的引号或空格
2. 确认 `api_hash` 没有多余的空格
3. 重新访问 https://my.telegram.org/apps 确认凭证是否正确

### 问题二：二维码扫描后没反应

**可能原因**：
1. 二维码已过期（一般只有几分钟有效期）
2. 网络无法访问 Telegram
3. Telegram 限制了登录

**解决方法**：
1. 关闭程序，重新运行 `python -m pagermaid` 获取新二维码
2. 检查网络是否正常
3. 尝试使用 Web 登录方式

### 问题三：启动后显示「已停止运行」

**原因**：可能是配置文件格式错误或缺少依赖。

**解决方法**：
1. 查看终端显示的错误信息
2. 确认 `data/config.yml` 文件格式正确（YAML 语法要求严格）
3. 重新安装依赖：`pip install -r requirements.txt`

### 问题四：找不到 data/config.yml 文件

**原因**：程序还没有生成配置文件。

**解决方法**：
1. 确认已进入项目目录：`cd PagerMaid-Pyro`
2. 确认已安装依赖：`pip install -r requirements.txt`
3. 尝试手动复制配置文件：
   ```bash
   cp config.gen.yml data/config.yml
   ```

### 问题五：如何切换回英文界面？

如果您想用回英文界面，可以修改配置文件：

打开 `data/config.yml`，找到：

```yaml
application_language: "zh-cn"
```

修改为：

```yaml
application_language: "en"
```

然后重启 Bot。

---

## ⚙️ 配置文件说明

主配置文件 `data/config.yml` 中常用的配置项如下：

```yaml
# ============ 核心配置 ============
api_id: "您的API_ID"           # Telegram 申请的应用 ID
api_hash: "您的API_HASH"       # Telegram 申请的应用 Hash

# ============ 登录设置 ============
qrcode_login: "False"         # 是否使用二维码登录（True/False）
web_login: "False"            # 是否使用 Web 登录（True/False）

# ============ 语言设置 ============
application_language: "zh-cn" # 语言设置：zh-cn 为中文，en 为英文
timezone: "Asia/Shanghai"     # 时区设置

# ============ Web 界面 ============
web_interface:
  enable: "False"             # 是否启用 Web 界面
  secret_key: "您的密码"      # Web 登录密码
  host: "127.0.0.1"          # 监听地址
  port: "3333"                # 监听端口

# ============ 日志设置 ============
log: "False"                  # 是否启用日志记录
log_chatid: "me"              # 日志发送到哪个聊天（me 表示自己）
```

---

## 📁 文件结构

```
PagerMaid-Pyro/
├── pagermaid/                # 主程序目录
│   ├── modules/              # 内置功能模块
│   ├── web/                  # Web 管理界面
│   ├── utils/                # 工具函数
│   └── config.py             # 配置文件
├── languages/                # 语言文件
│   └── built-in/
│       ├── zh-cn.yml         # 中文语言包 ⭐
│       └── en.yml            # 英文语言包
├── data/                     # 数据目录
│   ├── config.yml            # 配置文件 ⭐
│   ├── alias.json            # 命令别名
│   └── pagermaid.log.txt     # 日志文件
├── install_zh.py             # 一键汉化脚本 ⭐
├── requirements.txt          # Python 依赖
└── README_ZH.md              # 中文说明文档 ⭐
```

---

## 🔧 进阶操作

### 启用 Web 管理界面

1. 编辑 `data/config.yml`
2. 修改以下配置：

```yaml
web_interface:
  enable: "True"
  secret_key: "您的登录密码"
```

3. 重启 Bot
4. 打开浏览器访问 `http://127.0.0.1:3333`

### 安装插件

通过 Web 管理界面或以下命令安装插件：

```bash
# 列出可用插件
-apts list

# 安装插件
-apts install 插件名称
```

### 备份数据

建议定期备份以下文件：

- `data/config.yml` - 配置文件
- `data/alias.json` - 命令别名配置

---

## ⚠️ 注意事项

1. **API 凭证安全**：不要将您的 `api_id` 和 `api_hash`分享给他人
2. **首次使用**：建议先在测试群组中试用，熟悉功能后再正式使用
3. **插件来源**：请从可信来源安装插件，避免安全风险
4. **网络要求**：服务器需要能够访问 Telegram（大陆用户可能需要代理）
5. **登录限制**：同一个 Telegram 账号不能同时在多个设备登录 Bot

---

## 📞 获取帮助

如果遇到问题，您可以：

1. **查看日志**：`data/pagermaid.log.txt` 文件中可能有错误信息
2. **搜索引擎**：将错误信息复制到搜索引擎查找解决方案
3. **GitHub Issues**：访问项目 GitHub 页面提交问题

---

## 📝 更新日志

**版本 1.0.0**（当前版本）

- ✨ 首次发布深度汉化版
- 🌐 完成所有消息提示汉化
- 🎨 完成 Web 管理界面汉化
- 📖 编写详细中文安装文档
- 🔧 提供一键汉化安装脚本

---

<p align="center">
  感谢您使用 PagerMaid-Pyro 深度汉化版！
  
  如果这个项目对您有帮助，欢迎给个 Star ⭐
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made-with_❤️-red?style=for-the-badge" alt="Made with Love">
</p>
