import json
import aiofiles
from pathlib import Path
from typing import Set, Optional
import logging
from .config import plugin_config

logger = logging.getLogger(__name__)

class BadWordsLoader:
    def __init__(self):
        self.file_path = Path(plugin_config.data_path)
        self.badwords: Set[str] = set()

    async def load(self) -> Optional[Set[str]]:
        """异步加载违禁词列表"""
        try:
            if not await self._check_file():
                await self._init_default_file()
            
            async with aiofiles.open(self.file_path, "r", encoding="utf-8") as f:
                data = json.loads(await f.read())
                self.badwords = set(data.get("badwords", []))
                logger.info(f"成功加载 {len(self.badwords)} 条违禁词")
                return self.badwords
        except Exception as e:
            logger.error(f"违禁词加载失败: {str(e)}")
            return None

    async def _check_file(self) -> bool:
        """检查文件有效性"""
        if not self.file_path.exists():
            return False
        if self.file_path.is_dir():
            raise IsADirectoryError(f"{self.file_path} 是目录而非文件")
        return True

    async def _init_default_file(self):
        """初始化默认违禁词文件"""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        default_data = {"badwords": ["赌博", "色情", "诈骗", "毒品", "暴力"]}
        async with aiofiles.open(self.file_path, "w", encoding="utf-8") as f:
            await f.write(json.dumps(default_data, ensure_ascii=False, indent=2))
        logger.info(f"已创建默认违禁词文件：{self.file_path}")