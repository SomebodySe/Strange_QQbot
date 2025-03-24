import shlex

def modify_list(msg):
    try:
        # 读取文件内容
        with open("src/plugins/note.txt", 'r') as file:
            items = file.read().splitlines()
    except FileNotFoundError:
        # 如果文件不存在，创建一个空列表
        items = []

    if msg.startswith("删除"):
        content_to_delete = msg[2:].strip()  # 获取 "删除" 后的内容
        # 尝试将内容视为索引进行删除
        try:
            index_to_delete = int(content_to_delete) - 1  # 转换为索引（用户输入索引从1开始）
            if 0 <= index_to_delete < len(items):
                removed_item = items.pop(index_to_delete)  # 删除索引项
                with open("src/plugins/note.txt", 'w') as file:
                    file.write("\n".join(items))
                return f"已删除第 {index_to_delete + 1} 项: {removed_item}"
            else:
                return f"索引 {index_to_delete + 1} 超出范围。"
        except ValueError:
            # 如果不是索引，尝试直接匹配内容
            if content_to_delete in items:
                items.remove(content_to_delete)  # 删除匹配的内容
                with open("src/plugins/note.txt", 'w') as file:
                    file.write("\n".join(items))
                return f"已删除内容: {content_to_delete}"
            else:
                return f"内容 '{content_to_delete}' 不在列表中。"
    else:
        # 添加元素到列表
        if msg not in items:
            items.append(msg)
            with open("src/plugins/note.txt", 'w') as file:
                file.write("\n".join(items))
            return f"'{msg}' 已添加。"
        else:
            return f"'{msg}' 已存在于列表中。"


def show_list(file_name):
    try:
        # 显示列表内容
        with open(file_name, 'r') as file:
            items = file.read().splitlines()
        if items:
            result = ""
            for index, item in enumerate(items, start=1):  # 使用 enumerate 添加索引
                result += f"{index}: {item}\n"
            return result
        else:
            return "列表为空。"
    except FileNotFoundError:
        return "列表为空或文件不存在。"


def note(msgx):
    msg = msgx.split("note", 1)[1].strip()
    # 获取输入参数并处理引号与空格
    raw_input = msg
    search_term = shlex.split(raw_input)[0]
    file_name = "src/plugins/note.txt"

    # 如果参数是 "列表"，调用显示函数
    if search_term == "列表":
        return show_list(file_name)
    # 如果参数以 "删除" 开头，处理删除操作
    elif search_term.startswith("删除"):
        return modify_list(search_term)
    else:
        # 否则，将参数添加到列表
        return modify_list(search_term)


# print(note("note删除2"))