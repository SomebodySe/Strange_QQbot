from openai import OpenAI
from datetime import datetime
from src.plugins.init import *
from copy import deepcopy
import os


# 你的 DeepSeek API Key
def ai(msgx, group_id, user_id):
    messages = deepcopy(ai_role)

    if not messages[0]["content"]:
        return "禁止AI聊天：未定义发言规则"

    client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")
    mode = "deepseek-v4-flash"

    msg = msgx
    filename = f"{AI_DIR}/{group_id}_chat.txt"
    
    # 如果文件不存在，则创建
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("")

    # 读取历史消息
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        # 确保最后一行换行
        if lines and not lines[-1].endswith("\n"):
            lines[-1] = lines[-1] + "\n"
        # 追加当前用户输入
        msgx = msg.replace("\n", "  ")
        lines.append(f"{user_id}: {msgx}\n")
        
        if len(lines) > 57:
            lines = lines[-57:]
        # 清空文件并写入更新后的内容
        file.seek(0)
        file.truncate()
        file.writelines(lines)

    # 构造对话消息，限制最多 8 轮对话（即 16 条消息）
    

    for line in lines:
        id, msg = line.split(":", 1)
        id = id.strip()
        msg = msg.strip()
        if id == "0":
            role = "assistant"
            content = msg
        else:
            role = "user"
            content = f"[用户{id}]：{msg}"
        messages.append({"role": role, "content": content})


    # 调用 DeepSeek API
    response = client.chat.completions.create(
        model=mode,
        messages=messages,
        stream=False
    )

    # 获取大模型的回答
    reply = response.choices[0].message.content
    replyx = reply.replace("\n", "  ")
    print(replyx)
    # 将模型回答写入文件，保持对话历史
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"0: {replyx}\n")
    token = response.usage
    usage = (3*token.completion_tokens + 2*token.prompt_cache_miss_tokens + 0.2*token.prompt_cache_hit_tokens)/1000000
    print(f"usage:{usage}")

    usagefile = f"{AI_DIR}/{group_id}_usage.txt"
    with open(usagefile, "a+", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}]\n   chat:{usage}\n")
    with open(usagefile, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        if len(lines) > 2000:
            f.seek(0)
            f.writelines(lines[-2000:])
            f.truncate()

    return reply


def savemsg(msg, group_id, user_id):
    filename = f"{AI_DIR}/{group_id}_chat.txt"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("")
    msgx = msg.replace("\n", "  ")
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(f"{user_id}: {msgx}\n")


def getusage(group_id):
    try:
        with open(f"{AI_DIR}/{group_id}_usage.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return ''.join(lines[-30:]).strip()
    except FileNotFoundError:
        return "未找到记录"
    