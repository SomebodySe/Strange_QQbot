import subprocess

def py(msgx):
    msg = msgx.split("/py", 1)[1].strip()
    filename = "src/plugins/run.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(msg)
    result = subprocess.check_output(["python3", filename], text=True).strip()
    if len(result) > 1000:
        return result[-1000:]
    else:
        return result
