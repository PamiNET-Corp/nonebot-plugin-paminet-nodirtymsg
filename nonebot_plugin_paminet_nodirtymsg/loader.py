from nonebot import logger, require
from pathlib import Path
from typing import Set, Optional
import json
import aiofiles
from importlib import resources
from .config import plugin_config

# 使用 require 加载 nonebot_plugin_localstore
require("nonebot_plugin_localstore")
from nonebot_plugin_localstore import get_data_dir

class BadWordsLoader:
    def __init__(self):
        # 使用 localstore 获取数据目录
        data_dir = plugin_config.data_path or get_data_dir("paminet_nodirtymsg")
        self.file_path = Path(data_dir) / "badwords.json"
        self.badwords: Set[str] = set()
    
    async def load(self) -> Optional[Set[str]]:
        """异步加载违禁词列表"""
        try:
            if not await self._check_file():
                await self._release_default_file()  # 释放预制文件
            
            async with aiofiles.open(self.file_path, "r", encoding="utf-8") as f:
                data = json.loads(await f.read())
                self.badwords = set(data.get("badwords", []))
                logger.info(f"成功加载 {len(self.badwords)} 条违禁词")
                return self.badwords
        except Exception as e:
            logger.error(f"违禁词加载失败: {str(e)}")
            return None

    async def _check_file(self) -> bool:
        """检查文件是否存在且有效"""
        if not self.file_path.exists():
            return False
        if self.file_path.is_dir():
            raise IsADirectoryError(f"{self.file_path} 是目录而非文件")
        return True

    async def _release_default_file(self):
        """释放预制的 badwords.json 文件"""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        # 使用 importlib.resources 读取包内资源文件
        with resources.path("nonebot_plugin_paminet_nodirtymsg.data", "badwords.json") as src_path:
            async with aiofiles.open(src_path, "r", encoding="utf-8") as src, \
                         aiofiles.open(self.file_path, "w", encoding="utf-8") as dst:
                content = await src.read()
                await dst.write(content)
        logger.info(f"已释放默认违禁词文件到：{self.file_path}")