def status(msg):
    from mcstatus import JavaServer
    try:
        params = msg.split("服务器状态", 1)[1].strip()
        if not params:
            filename = "src/plugins/iplist.txt"
            servers = []
            result = ""
            with open(filename, "r") as f:
                for line in f:
                    name, ip = line.strip().split()
                    servers.append({"name": name, "ip": ip})
            # 遍历服务器列表
            for server in servers:
                result += f"服务器：{server['name']}\n"
                result += f"IP：{server['ip']}\n"
                try:
                    status = JavaServer.lookup(server["ip"]).status()
                except Exception as e:
                    result += f"服爆辣！（{str(e)}）\n\n"
                else:
                    result += f"在线人数：{status.players.online}\n"
                    if status.players.online != 0 and status.players.sample:
                        result += f"玩家列表：{', '.join([player.name for player in status.players.sample])}\n"
                    latency = JavaServer.lookup(server["ip"]).ping()
                    result += f"ping：{int(latency)}\n\n"
            return result.strip()
        server_address = params  # 如果有参数，使用第一个参数作为服务器地址
        server = JavaServer.lookup(server_address)
        result = ""
        result += f"服务器地址：{server_address}\n"
        try:
            status = server.status()
        except Exception as e:
            result += f"服爆辣！（{str(e)}）\n\n"
        else:
            result += f"在线人数：{status.players.online}\n"
            if status.players.online != 0:
                result += f"玩家列表：{', '.join([player.name for player in status.players.sample])}\n"
            latency = server.ping()
            result += f"ping：{int(latency)}\n\n"
            return result.strip()

    except Exception as e:
        return f"运行脚本时发生错误: {e}"

#print(status("服务器状态"))