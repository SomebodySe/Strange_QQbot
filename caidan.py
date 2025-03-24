def caidan():
    try:
        with open("src/plugins/caidan.txt", 'r') as file:
            content = file.read()
        return content  # 输出文件内容
    except FileNotFoundError:
        return f"文件不存在。"

# print(caidan())