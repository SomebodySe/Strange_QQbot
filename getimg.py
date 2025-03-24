from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
import aiohttp
import aiofiles
import os

# 指定要监听的群组ID
TARGET_GROUP_ID = 980594025  # 替换为实际的群组ID 1004031354 980594025

# 定义一个处理群消息的处理器，仅监听指定群组
save_emoticon = on_message(priority=5, block=False)

@save_emoticon.handle()
async def handle_message(bot: Bot, event: GroupMessageEvent):
    # 检查是否为指定的群组
    if event.group_id != TARGET_GROUP_ID:
        return

    msg = event.message

    # 检查消息中是否包含图片
    for seg in msg:
        if seg.type == "image":
            # 获取图片URL
            image_url = seg.data["url"]
            with open('src/plugins/image.txt', 'w', encoding='utf-8') as file:
                file.write(image_url)
