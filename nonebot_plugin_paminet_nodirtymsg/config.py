from pydantic import BaseModel, Field
from nonebot import get_plugin_config

class PluginConfig(BaseModel):
    enable_filter: bool = Field(default=True, description="是否启用违禁词过滤")
    allow_images: bool = Field(default=False, description="是否允许图片消息")
    data_path: str = Field(default="", description="数据存储路径")
    max_retries: int = Field(default=3, description="消息撤回重试次数")

# 加载插件配置
plugin_config = get_plugin_config(PluginConfig)