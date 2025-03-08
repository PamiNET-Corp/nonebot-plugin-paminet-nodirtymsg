from nonebot.plugin import PluginMetadata
from .config import PluginConfig

__plugin_meta__ = PluginMetadata(
    name="No Dirty Message",
    description="基于Trie树的高效群聊违禁词过滤插件，用于撤回群成员们逆天发言的Nonebot2插件.由DeepSeek-R1辅助开发.",
    usage="自动撤回群成员的敏感发言。需要管理员权限.",
    type="application",
    homepage="https://github.com/PamiNET-Corp/nonebot-plugin-paminet-nodirtymsg",
    config=PluginConfig,
    supported_adapters={"~onebot.v11"},
    extra={
        "version": "0.2.0",
        "author": "PamiNET",
        "license": "MIT",
    },
)

from .handler import dirty_msg_filter