import shlex, os

# Function to read IPs from file and return as a list of dictionaries
def read_ips(filename):
    # 如果文件不存在则创建空文件
    if not os.path.exists(filename):
        open(filename, 'w').close()  # 创建空文件

    ips = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:  # 跳过空行
                continue
            parts = line.split()
            if len(parts) == 2:
                name, ip = parts
                ips.append({'name': name, 'ip': ip})
    return ips

# Function to save IPs to file
def save_ips(filename, ips):
    with open(filename, 'w') as f:
        for ip in ips:
            f.write(f"{ip['name']} {ip['ip']}\n")

# Function to print IPs with index
def print_ips(ips):
    result = ""
    for i, ip in enumerate(ips):
        result += f"{i}: {ip['name']} {ip['ip']}\n"
    return result

# Function to add IP to list
def add_ip(filename, name, ip):
    ips = read_ips(filename)
    ips.append({'name': name, 'ip': ip})
    save_ips(filename, ips)

# Function to delete IP from list by index
def delete_ip(filename, index):
    ips = read_ips(filename)
    if 0 <= index < len(ips):
        del ips[index]
        save_ips(filename, ips)

# Main function to handle command-line arguments
def ip(msgx, group_id):
    msg = msgx.split("/ip", 1)[1].strip()
    filename = f"src/plugins/ip/{group_id}.txt"  # Your IP list file

    if len(msg) < 2:
        return  # No arguments, do nothing

    # 获取完整参数字符串，并使用 shlex.split() 拆分
    full_command = msg
    args = shlex.split(full_command)
    if not args:
        return  # 没有参数则退出

    command = args[0]

    if command == "list":
        ips = read_ips(filename)
        return print_ips(ips)
    elif command == "add" and len(args) > 2:
        name = args[1]
        ip = args[2]
        add_ip(filename, name, ip)
        return f"Added: {name} {ip}"
    elif command == "del" and len(args) > 1:
        index = int(args[1])
        delete_ip(filename, index)
        return f"Deleted index: {index}"
    else:
        return "Invalid command or arguments."

#print(ip("/iplist"))

