from nonebot.plugin import PluginMetadata

from .config import PluginConfig
from .main import dirty_msg_filter

__plugin_meta__ = PluginMetadata(
    name="No Dirty Message",
    description="用于撤回群成员们逆天发言的Nonebot2插件.由DeepSeek-R1辅助开发.",
    usage="自动撤回群成员的敏感发言。需要管理员权限.",
    type="application",
    homepage="https://github.com/PamiNET-Corp/nonebot-plugin-paminet-nodirtymsg",
    config=PluginConfig,
    supported_adapters={"~onebot.v11"},
    extra={
        "version": "0.1.0",
        "author": "PamiNET",
        "license": "MIT",
    },
)

# 导出插件功能
__all__ = ["dirty_msg_filter"]