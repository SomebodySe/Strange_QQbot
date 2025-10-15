from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from src.plugins import imageadd,features
import requests
import imghdr
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
        if seg.type == "image" or seg.type == "mface":
            # 获取图片URL
            image_url = seg.data["url"]
            
            filename = f"src/plugins/lastimage/{group_id}.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(image_url)

            if imageadd.imageadd(image_url,group_id):
                content = requests.get(image_url).content
                ext = imghdr.what(None, content)
                save_path = f"src/plugins/imageadd/addimage.{ext}"
                with open(save_path, 'wb') as f:
                    f.write(content)
                image_path = os.path.abspath(f"src/plugins/imageadd/addimage.{ext}")
                await bot.send_group_msg(group_id=group_id, message=MessageSegment.image(f"file://{image_path}"))
                print("图片相同")
            else:
                print("图片不同")


