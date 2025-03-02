<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-paminet-nodirtymsg

_✨ NoneBot 群聊脏话管理插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/PamiNET-Corp/nonebot-plugin-paminet-nodirtymsg.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-paminet-nodirtymsg">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-paminet-nodirtymsg.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

## 📖 介绍
#### 只是一个平平无奇的聊天过滤插件。  
#### 暂仅支持OnebotV11协议
> [!WARN]
> **该项目由DeepSeek-R1辅助开发！**

> [!IMPORTANT]
> **收藏项目**，让更多人知道这个没什么用的东西！⭐️

<img width="100%" src="https://starify.komoridevs.icu/api/starify?owner=PamiNET-Corp&repo=nonebot-plugin-paminet-nodirtymsg" alt="starify" />

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-paminet-nodirtymsg

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-paminet-nodirtymsg
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-paminet-nodirtymsg
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-paminet-nodirtymsg
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-paminet-nodirtymsg
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_template"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| enable_dirty_msg_filter | 否 | True | 是否启用聊天过滤 |

## 🎉 使用
### 指令表
用去吧孩子，没指令
### 效果图
如果有效果图的话暂无

## 📄 许可证

本项目使用 [MIT](./LICENSE) 许可证开源

```txt
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```