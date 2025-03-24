from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from src.plugins import status,mcwiki,gtwiki,ip,caidan,note
# 定义一个处理群消息的处理器
group_message_handler = on_message(priority=9, block=True)


@group_message_handler.handle()
async def handle_group_message(bot: Bot, event: GroupMessageEvent):
    # 获取群号和发送者ID
    group_id = 123456789
    if event.group_id != group_id:
        return
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
    elif msg == "撸猫":
        await bot.send_group_msg(group_id=group_id, message=MessageSegment.at(1838184387) + "\n〈.>ᯅ<.〉\n ( つाूीु⊂ )\n撸撸need")
    elif msg == "菜单":
        await bot.send_group_msg(group_id=group_id, message=caidan.caidan())
    elif msg.startswith("note"):
        await bot.send_group_msg(group_id=group_id, message=note.note(msg))
    elif msg.startswith("/send"):
        await bot.send_group_msg(group_id=group_id, message=msg.split("/send", 1)[1].strip())
    elif msg == "":
        return
    elif msg == "提取表情":
        with open('src/plugins/image.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
        await bot.send_group_msg(group_id=group_id, message=file_content)
    #elif msg == "/test":
    else:
        with open('src/plugins/textadd.txt', 'r+', encoding='utf-8') as file:
            if file.read() != msg:
                file.seek(0)  # 将文件指针移动到开头
                file.truncate()  # 清空文件内容
                file.write(msg)  # 写入新的字符串
            else:
                await bot.send_group_msg(group_id=group_id, message=msg)
                file.seek(0)
                file.truncate()
                file.write("!)@(#*$&fill")
