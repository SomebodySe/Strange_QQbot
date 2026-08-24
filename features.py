def features():
    try:
        with open("src/plugins/features.txt", 'r') as file:
            content = file.read()
        return content  # 输出文件内容
    except FileNotFoundError:
        return f"未定义功能列表"

# print(caidan())