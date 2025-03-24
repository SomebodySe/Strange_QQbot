
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from src.plugins import status, mcwiki, gtwiki, ip, caidan, note
import os

# 定义一个处理群消息的处理器
group_message_handler = on_message(priority=9, block=True)


@group_message_handler.handle()
async def handle_group_message(bot: Bot, event: GroupMessageEvent):
    # 获取群号和发送者ID
    group_id = 980594025  # 1004031354  980594025
    # 获取消息内容
    msg = event.get_plaintext()
    if msg == "提取表情":
        with open('src/plugins/image.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
        await bot.send_group_msg(group_id=group_id, message=file_content)

