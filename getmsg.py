from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from src.plugins import status,geturl,addr,features,note,ai,py,addone
from src.plugins.init import *
import os, re, regex

# 定义一个处理群消息的处理器
group_message_handler = on_message(priority=9, block=True)
init()

@group_message_handler.handle()
async def handle_group_message(bot: Bot, event: GroupMessageEvent):
    print("EVENT: ", event)
    group_id = event.group_id

    if group_id not in groups:
        print("不在部署群聊列表中")
        return
    
    user_id = event.user_id
    msg = event.get_plaintext()
    if msg.startswith("服务器状态"):
        await bot.send_group_msg(group_id=group_id, message=status.status(msg, group_id))
    elif event.is_tome():
        await bot.send_group_msg(group_id=group_id, message=parse_at_message(ai.ai(msg, group_id, user_id)))
    elif msg.startswith("/aiusage"):
        await bot.send_group_msg(group_id=group_id, message=ai.getusage(group_id))
    elif msg.startswith("/mc"):
        await bot.send_group_msg(group_id=group_id, message=geturl.mcwiki(msg))
    elif msg.startswith("/gt"):
        await bot.send_group_msg(group_id=group_id, message=geturl.gtwiki(msg))
    elif msg.startswith("/addr"):
        await bot.send_group_msg(group_id=group_id, message=addr.addr(msg, group_id))
    elif msg == "功能菜单":
        await bot.send_group_msg(group_id=group_id, message=features.features())
    elif msg.startswith("note"):
        await bot.send_group_msg(group_id=group_id, message=note.note(msg, group_id).strip())
    elif msg.startswith("/py"):
        if user_id == ROOT_ID:
            await bot.send_group_msg(group_id=group_id, message=py.py(msg))
        else:
            await bot.send_group_msg(group_id=group_id, message="无权限！")
    elif msg.startswith("/pip"):
        if user_id == ROOT_ID:
            await bot.send_group_msg(group_id=group_id, message=py.pip(msg))
        else:
            await bot.send_group_msg(group_id=group_id, message="无权限！")
    elif msg == " ":
        return
    elif regex.fullmatch(r'\s*\X\s*\+\s*\X\s*', msg):
        return
    elif msg.startswith("["):
        return
    elif msg == "图片链接":
        filename = f"{LAST_IMG_DIR}/{group_id}.txt"
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.read()
        await bot.send_group_msg(group_id=group_id, message=file_content)
    elif msg == "":
        filename = f"{TXT_ADD_DIR}/{group_id}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"……empty……|\\|1")
    else:
        addone.setempty(group_id)
        ai.savemsg(msg, group_id, user_id)
        if addone.textadd(msg, group_id):
           await bot.send_group_msg(group_id=group_id, message=msg)
        

def parse_at_message(text):
    msg = MessageSegment.text("")  # 初始化空消息段
    # 匹配形如 [@123456789] 的部分
    parts = re.split(r'(\[@\d{5,12}\])', text)

    for part in parts:
        if re.fullmatch(r'\[@\d{5,12}\]', part):
            qq = int(part[2:-1])  # 去掉前缀 "[@" 和后缀 "]"
            msg += MessageSegment.at(qq)
        elif part:
            msg += MessageSegment.text(part)

    return msg