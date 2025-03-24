import os

def textadd(msg, group_id):
    filename = f"src/plugins/textadd/{group_id}.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("!)@(#*$&create")
    with open(filename, 'r+', encoding='utf-8') as file:
        if file.read() != msg:
            file.seek(0)  # 将文件指针移动到开头
            file.truncate()  # 清空文件内容
            file.write(msg)  # 写入新的字符串
            return 0
        else:
            file.seek(0)
            file.truncate()
            file.write("!)@(#*$&fill")
            return 1
