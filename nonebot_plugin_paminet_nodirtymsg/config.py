import os
from nonebot import get_driver
from pydantic import BaseModel, Field

class PluginConfig(BaseModel):
    enable_filter: bool = Field(
        default=True,
        alias="DIRTY_MSG_FILTER_ENABLE",
        description="是否启用违禁词过滤"
    )
    allow_images: bool = Field(
        default=False,
        alias="ALLOW_IMAGES",
        description="是否允许图片消息"
    )
    data_path: str = Field(
        default=os.path.join("data", "badwords.json"),
        alias="BADWORDS_DATA_PATH",
        description="违禁词文件路径（支持绝对路径）"
    )
    max_retries: int = Field(
        default=3,
        alias="MAX_RETRIES",
        description="消息撤回重试次数"
    )

driver = get_driver()
global_config = driver.config
plugin_config = PluginConfig(**global_config.dict())