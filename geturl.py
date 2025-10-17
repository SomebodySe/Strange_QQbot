from urllib.parse import quote


def gtwiki(msg):
    params = msg.split("/gt", 1)[1].strip()
    if not params:
        return "gtnh.huijiwiki.com"
    
    encoded_query = quote(params, encoding='utf-8')
    base_url = "https://gtnh.huijiwiki.com/index.php"
    search_query = f"?profile=default&search={encoded_query}"
    url = base_url + search_query
    return url


def mcwiki(msg):
    params = msg.split("/mc", 1)[1].strip()
    if not params:
        return "mcmod.cn"
    
    encoded_query = quote(params, encoding='utf-8')
    base_url = "https://search.mcmod.cn/s"
    search_query = f"?key={encoded_query}"
    url = base_url + search_query
    return url
