from nonebot import logger, require
from pathlib import Path
from typing import Set, Optional
import json
import aiofiles

require("nonebot_plugin_localstore")
from nonebot_plugin_localstore import get_plugin_data_dir

class BadWordsLoader:
    def __init__(self):
        self.data_dir = get_plugin_data_dir()
        self.file_path = self.data_dir / "badwords.json"
        self.badwords: Set[str] = set()
    
    async def load(self) -> Optional[Set[str]]:
        """异步加载违禁词列表"""
        try:
            if not await self._check_file():
                await self._release_default_file()
            
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
        # 使用 pathlib 获取预制文件路径
        default_file = Path(__file__).parent / "data/badwords.json"
        async with aiofiles.open(default_file, "r", encoding="utf-8") as src, \
                     aiofiles.open(self.file_path, "w", encoding="utf-8") as dst:
            content = await src.read()
            await dst.write(content)
        logger.info(f"已释放默认违禁词文件到：{self.file_path}")