import os
import hashlib
import requests

def same(url1, url2):
    try:
        print(url1)
        # 下载两张图片的内容
        response1 = requests.get(url1)
        response2 = requests.get(url2)

        # 检查响应是否成功
        if response1.status_code != 200 or response2.status_code != 200:
            print("图片下载失败")
            return 0

        # 计算 SHA256 哈希值
        hash1 = hashlib.sha256(response1.content).hexdigest()
        hash2 = hashlib.sha256(response2.content).hexdigest()

        # 比较哈希值
        return 1 if hash1 == hash2 else 0

    except Exception as e:
        print("错误：", e)
        return 0


def setempty(group_id):
    filename = f"src/plugins/imageadd/{group_id}.txt"
    with open(filename, 'w') as file:
        file.write("empty")


def imageadd(msg, group_id):
    filename = f"src/plugins/imageadd/{group_id}.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("empty")
        return 0
    with open(filename, 'r+', encoding='utf-8') as file:
        url1 = file.read()
        if url1 == "empty":
            file.seek(0)  # 将文件指针移动到开头
            file.truncate()  # 清空文件内容
            file.write(msg)  # 写入新的字符串
            return 0
        elif not same(url1, msg):
            file.seek(0)  # 将文件指针移动到开头
            file.truncate()  # 清空文件内容
            file.write(msg)  # 写入新的字符串
            return 0
        else:
            file.seek(0)
            file.truncate()
            file.write("empty")
            return 1
