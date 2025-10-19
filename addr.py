import shlex, os

# Function to read IPs from file and return as a list of dictionaries
def read_addr(filename):
    # 如果文件不存在则创建空文件
    if not os.path.exists(filename):
        open(filename, 'w').close()  # 创建空文件

    addr = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:  # 跳过空行
                continue
            parts = line.split()
            if len(parts) == 2:
                name, ad = parts
                addr.append({'name': name, 'addr': ad})
    return addr

# Function to save IPs to file
def save_addr(filename, addr):
    with open(filename, 'w') as f:
        for ad in addr:
            f.write(f"{ad['name']} {ad['addr']}\n")

# Function to print IPs with index
def print_addr(addr):
    result = ""
    for i, ad in enumerate(addr):
        result += f"{i}: {ad['name']} {ad['addr']}\n"
    return result

# Function to add IP to list
def add_ad(filename, name, ad):
    addr = read_addr(filename)
    addr.append({'name': name, 'addr': ad})
    save_addr(filename, addr)

# Function to delete IP from list by index
def delete_ad(filename, index):
    addr = read_addr(filename)
    if 0 <= index < len(addr):
        del addr[index]
        save_addr(filename, addr)

# Main function to handle command-line arguments
def addr(msgx, group_id):
    msg = msgx.split("/addr", 1)[1].strip()
    filename = f"src/plugins/addr/{group_id}.txt"  # Your IP list file

    if len(msg) < 2:
        return  # No arguments, do nothing

    # 获取完整参数字符串，并使用 shlex.split() 拆分
    full_command = msg
    args = shlex.split(full_command)
    if not args:
        return  # 没有参数则退出

    command = args[0]

    if command == "list":
        addr = read_addr(filename)
        return print_addr(addr)
    elif command == "add" and len(args) > 2:
        name = args[1]
        ad = args[2]
        add_ad(filename, name, ad)
        return f"Added: {name} {ad}"
    elif command == "del" and len(args) > 1:
        index = int(args[1])
        delete_ad(filename, index)
        return f"Deleted index: {index}"
    else:
        return "Invalid command or arguments."

