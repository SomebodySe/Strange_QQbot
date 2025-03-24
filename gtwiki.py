from urllib.parse import quote

def generate_url(query):
    # 将参数转为 URL 编码
    encoded_query = quote(query, encoding='utf-8')

    # 拼接 URL
    base_url = "https://gtnh.huijiwiki.com/index.php"
    search_query = f"?search={encoded_query}"
    return base_url + search_query


def gtwiki(msg):
    try:
        params = msg.split("/gt", 1)[1].strip()
        if not params:
            return "gtnh.huijiwiki.com"
        url = generate_url(params)
        return url
    except Exception as e:
        return f"运行脚本时发生错误: {e}"

# print(gtwiki("/gt"))