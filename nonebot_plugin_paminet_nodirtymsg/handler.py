from nonebot import on_message, get_driver
from nonebot.adapters.onebot.v11 import MessageEvent, Bot
from nonebot.matcher import Matcher
from nonebot.log import logger
from .config import plugin_config
from .loader import BadWordsLoader
from .filter import BadWordsFilter
import asyncio

dirty_msg_filter = on_message(priority=5, block=True)

# 初始化组件
loader = BadWordsLoader()
filter = BadWordsFilter()

async def initialize():
    """异步初始化违禁词过滤器"""
    words = await loader.load()
    if words:
        filter.build(words)
        logger.success("违禁词过滤器初始化完成")
    else:
        logger.warning("违禁词列表为空，过滤器未启用")

# 使用 nonebot 的生命周期钩子
driver = get_driver()

@driver.on_startup
async def startup():
    await initialize()

@dirty_msg_filter.handle()
async def handle_event(event: MessageEvent, bot: Bot):
    if not plugin_config.enable_filter:
        return
    
    if event.message_type != "group":
        return
    
    if filter.search(event.raw_message):
        await retry_delete(bot, event.message_id)

async def retry_delete(bot: Bot, msg_id: int):
    for i in range(plugin_config.max_retries):
        try:
            await bot.delete_msg(message_id=msg_id)
            logger.info(f"消息 {msg_id} 撤回成功")
            return
        except Exception as e:
            logger.warning(f"撤回尝试 {i+1}/{plugin_config.max_retries} 失败: {str(e)}")
            await asyncio.sleep(1)
    
    logger.error(f"消息 {msg_id} 撤回失败，已达最大重试次数")