from dataclasses import dataclass
from nonebot import get_plugin_config

@dataclass
class PluginConfig:
    enable_filter: bool = True
    allow_images: bool = False
    data_path: str = ""
    max_retries: int = 5

# 加载插件配置
plugin_config = get_plugin_config(PluginConfig)