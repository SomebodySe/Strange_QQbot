import subprocess, shlex

def py(msgx):
    msg = msgx.split("/py", 1)[1].strip()
    filename = "src/plugins/run.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(msg)
    try:
        # 把 stderr 合并到 stdout
        result = subprocess.check_output(
            ["python3", filename],
            text=True,
            timeout=5,
            stderr=subprocess.STDOUT
        ).strip()
    except subprocess.TimeoutExpired:
        return("运行超时")
    except subprocess.CalledProcessError as e:
        result = f"错误:\n{e.output}"
    if len(result) > 1000:
        return result[-1000:]
    elif result == "":
        return "无输出"
    else:
        return result


def pip(msgx):
    msg = msgx.split("/", 1)[1].strip()
    if msg.startswith("pip uninstall "):
        msg += " -y"
    cmd = ["conda", "run", "-n", "test"] + shlex.split(msg)
    try:
        result = subprocess.check_output(cmd, text=True, timeout=1000).strip()
    except subprocess.TimeoutExpired:
        return("运行超时")
    except subprocess.CalledProcessError as e:
        return f"命令错误:\n{e.output}"

    result = result.replace('.', '. ').replace(':', ': ')

    if len(result) > 1000:
        return result[-1000:]
    elif result == "":
        return "无输出"
    else:
        return result
