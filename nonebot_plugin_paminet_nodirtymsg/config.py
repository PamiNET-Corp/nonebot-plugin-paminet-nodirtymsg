# config.py

from nonebot import Config

class PluginConfig(Config):
    # 是否启用违禁词检测
    enable_dirty_msg_filter: bool = True

    # 是否允许图片
    allow_images: bool = False

# 实例化配置项
config = PluginConfig()
