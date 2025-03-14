from nonebot import get_plugin_config
from typing import Optional

class PluginConfig:
    enable_filter: bool = True
    allow_images: bool = False
    data_path: Optional[str] = None
    max_retries: int = 3

# 加载插件配置
plugin_config = get_plugin_config(PluginConfig)