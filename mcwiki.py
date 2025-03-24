from urllib.parse import quote

def generate_url(query):
    # 将参数转为 URL 编码
    encoded_query = quote(query, encoding='utf-8')

    # 拼接 URL
    base_url = "https://search.mcmod.cn/s"
    search_query = f"?key={encoded_query}"
    return base_url + search_query

def mcwiki(msg):
    try:
        params = msg.split("/mc", 1)[1].strip()
        if not params:
            return "mcmod.cn"
        url = generate_url(params)
        return url
    except Exception as e:
        return f"运行脚本时发生错误: {e}"

#print(mcwiki("/mc蒸汽"))
