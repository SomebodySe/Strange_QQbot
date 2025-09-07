import os
import hashlib
import requests

def same(url1, url2):
    """比较两张图片是否相同"""
    try:
        # 下载两张图片
        response1 = requests.get(url1)
        response2 = requests.get(url2)

        # 检查响应是否成功
        if response1.status_code != 200 or response2.status_code != 200:
            print("图片下载失败")
            return False

        # 计算 SHA256 哈希值
        hash1 = hashlib.sha256(response1.content).hexdigest()
        hash2 = hashlib.sha256(response2.content).hexdigest()

        # 比较哈希值
        return hash1 == hash2

    except Exception as e:
        print("错误：", e)
        return False


def setempty(group_id):
    """重置状态"""
    filename = f"src/plugins/imageadd/{group_id}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("empty|0")


def imageadd(msg, group_id):
    """
    图片+1逻辑：
    - 文件格式 url|index
    - 同一张图且index=0 -> 改为index=1返回1(执行+1)
    - 同一张图且index=1 -> 不动返回0
    - 不同图 -> 重置url|0返回0
    """
    filename = f"src/plugins/imageadd/{group_id}.txt"
    if not os.path.exists(filename):
        # 初始化文件
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{msg}|0")
        return 0

    with open(filename, 'r+', encoding='utf-8') as file:
        content = file.read().strip()
        if '|' in content:
            old_url, idx_str = content.rsplit('|', 1)
            try:
                idx = int(idx_str)
            except ValueError:
                old_url, idx = "empty", 0
        else:
            old_url, idx = content, 0

        # 如果是空状态或者不同图片
        if old_url == "empty" or not same(old_url, msg):
            file.seek(0)
            file.truncate()
            file.write(f"{msg}|0")
            return 0

        # 同一张图片
        if idx == 0:
            # 改为index=1，表示执行+1
            file.seek(0)
            file.truncate()
            file.write(f"{old_url}|1")
            return 1
        else:
            # 已经+1过了，不再+1
            return 0
