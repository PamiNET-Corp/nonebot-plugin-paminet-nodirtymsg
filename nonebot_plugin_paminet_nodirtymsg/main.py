# main.py

import json
import os
from nonebot import on_message
from nonebot.adapters.onebot.v11 import MessageEvent, Bot
from nonebot.matcher import Matcher
from nonebot.log import logger
from .config import config

# 加载违禁词
def load_badwords():
    try:
        # 获取插件目录的绝对路径
        plugin_dir = os.path.dirname(__file__)
        file_path = os.path.join(plugin_dir, "data", "badwords.json")
        logger.info(f"加载违禁词文件路径: {file_path}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data.get("badwords", []))
    except Exception as e:
        logger.error(f"加载违禁词失败: {e}")
        return set()

# 初始化违禁词
badwords = load_badwords()

# 明确指定 dirty_msg_filter 的类型为 Matcher
dirty_msg_filter: Matcher = on_message(priority=5, block=True)

@dirty_msg_filter.handle()
async def handle_dirty_msg(event: MessageEvent, bot: Bot, matcher: Matcher):
    if not config.enable_dirty_msg_filter:
        return  # 如果插件被禁用，则不处理

    # 判断消息是否为群聊消息
    if event.message_type == "group":
        # 遍历消息并检查违禁词
        for word in badwords:
            if word in event.raw_message:
                # 如果包含违禁词，则撤回消息
                try:
                    await bot.delete_msg(message_id=event.message_id)
                    logger.info(f"撤回群消息，消息ID：{event.message_id}，内容包含违禁词：{word}")
                except Exception as e:
                    logger.error(f"撤回消息失败：{e}")
                break
