from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from src.plugins import status,mcwiki,gtwiki,ip,caidan,note,textadd,ai,py,page,imageadd
import os

# 定义一个处理群消息的处理器
group_message_handler = on_message(priority=9, block=True)


@group_message_handler.handle()
async def handle_group_message(bot: Bot, event: GroupMessageEvent):
    # 获取群号和发送者ID
    group_id = event.group_id
    send_id = 12345
    # 获取消息内容
    msg = event.get_plaintext()
    if msg.startswith("服务器状态"):
        await bot.send_group_msg(group_id=group_id, message=status.status(msg))
    elif msg.startswith("/mc"):
        await bot.send_group_msg(group_id=group_id, message=mcwiki.mcwiki(msg))
    elif msg.startswith("/gt"):
        await bot.send_group_msg(group_id=group_id, message=gtwiki.gtwiki(msg))
    elif msg.startswith("/ip"):
        await bot.send_group_msg(group_id=group_id, message=ip.ip(msg))
    elif msg.startswith("常用网址"):
        await bot.send_group_msg(group_id=group_id, message=page.page(msg, group_id))
    elif msg == "撸猫":
        await bot.send_group_msg(group_id=group_id, message=MessageSegment.at(1838184387) + "\n〈.>ᯅ<.〉\n ( つाूीु⊂ )\n撸撸need")
    elif msg == "菜单":
        await bot.send_group_msg(group_id=group_id, message=caidan.caidan())
    elif msg.startswith("note"):
        await bot.send_group_msg(group_id=group_id, message=note.note(msg, group_id).strip())
    elif msg.startswith("/ai"):
        await bot.send_group_msg(group_id=group_id, message=ai.ai(msg, group_id))
    elif msg.startswith("/send"):
        await bot.send_group_msg(group_id=send_id, message=msg.split("/send", 1)[1])
    elif msg.startswith("/py"):
        await bot.send_group_msg(group_id=group_id, message=py.py(msg))
    elif msg == "":
        return
    elif msg == " ":
        return
    elif msg.startswith("["):
        return
    # elif msg == "提取表情":
    #     filename = f"src/plugins/imageadd/{group_id}.txt"
    #     with open(filename, 'r', encoding='utf-8') as file:
    #         file_content = file.read()
    #     await bot.send_group_msg(group_id=group_id, message=file_content)
    elif msg == "/test":
        filename = f"src/plugins/imageadd/{group_id}.txt"
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.read()
        image_path = os.path.abspath("src/plugins/1.png")
        await bot.send_group_msg(group_id=group_id, message=MessageSegment.image(f"file://{image_path}"))
    else:
        imageadd.setempty(group_id)
        if textadd.textadd(msg, group_id):
            await bot.send_group_msg(group_id=group_id, message=msg)


        
