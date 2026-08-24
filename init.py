import os

BASE_DIR = "src/plugins"
ADDR_DIR = f"{BASE_DIR}/addr"
AI_DIR = f"{BASE_DIR}/ai"
IMG_ADD_DIR = f"{BASE_DIR}/addone/imageadd"
LAST_IMG_DIR = f"{BASE_DIR}/lastimage"
TXT_ADD_DIR = f"{BASE_DIR}/addone/textadd"
NOTE_DIR = f"{BASE_DIR}/note"
ROOT_ID = 123456

groups = {123456, 1234567}

API_KEY = "sk-xxxxx"   # 大模型API Key

filename = f"{BASE_DIR}/ai_role.txt"
try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:   
    content = ""
ai_role = [{"role": "system", "content": content}]

def init():
    dirs = [ADDR_DIR, AI_DIR, IMG_ADD_DIR, LAST_IMG_DIR, TXT_ADD_DIR, NOTE_DIR]
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
    

