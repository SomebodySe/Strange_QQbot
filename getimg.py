from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
import aiohttp
import aiofiles
import os

# 定义一个处理群消息的处理器，仅监听指定群组
save_emoticon = on_message(priority=5, block=False)

@save_emoticon.handle()
async def handle_message(bot: Bot, event: GroupMessageEvent):
    # 检查是否为指定的群组
    group_id = event.group_id

    msg = event.message

    # 检查消息中是否包含图片
    for seg in msg:
        if seg.type == "image":
            # 获取图片URL
            image_url = seg.data["url"]
            filename = f"src/plugins/imageadd/{group_id}.txt"
            with open(filename, 'w') as file:
                file.write(image_url)
