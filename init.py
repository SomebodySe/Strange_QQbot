import os

BASE_DIR = "src/plugins"
ADDR_DIR = f"{BASE_DIR}/addr"
AI_DIR = f"{BASE_DIR}/ai"
IMG_ADD_DIR = f"{BASE_DIR}/addone/imageadd"
LAST_IMG_DIR = f"{BASE_DIR}/lastimage"
TXT_ADD_DIR = f"{BASE_DIR}/addone/textadd"
NOTE_DIR = f"{BASE_DIR}/note"


def init():
    dirs = [ADDR_DIR, AI_DIR, IMG_ADD_DIR, LAST_IMG_DIR, TXT_ADD_DIR, NOTE_DIR]
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
            
