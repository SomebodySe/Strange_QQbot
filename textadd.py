import os

def textadd(msg, group_id):
    filename = f"src/plugins/textadd/{group_id}.txt"
    if not os.path.exists(filename):
        # 文件不存在时初始化
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{msg}|0")
        return 0 

    with open(filename, 'r+', encoding='utf-8') as file:
        content = file.read().strip()

        if '|' in content:
            old_msg, idx_str = content.rsplit('|', 1)
            try:
                idx = int(idx_str)
            except ValueError:
                # 异常情况重置
                old_msg, idx = '', 0
        else:
            old_msg, idx = content, 0

        if old_msg == msg:
            if idx == 0:
                # 改为索引1表示+1
                file.seek(0)
                file.truncate()
                file.write(f"{msg}|1")
                return 1  # 执行+1
            else:
                # 已经+1过了，不动
                return 0
        else:
            # 新消息，重置为索引0
            file.seek(0)
            file.truncate()
            file.write(f"{msg}|0")
            return 0
