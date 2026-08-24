# 需要的库：
```bash
# 基于nonebot2
pip install nb-cli  nonebot2[fastapi] nonebot-adapter-onebot 
pip install openai mcstatus regex
```



# 接入NapCat示例：
在napcat/config/onebot相应配置文件中的websocketClients加入：
```bash
      {
        "name": "WsClient",
        "enable": true,
        "url": "ws://127.0.0.1:8080/onebot/v11/ws",
        "messagePostFormat": "array",
        "reportSelfMessage": false,
        "reconnectInterval": 5000,
        "token": "12345ABCDE",
        "debug": false,
        "heartInterval": 30000
      }
```

nonebot路径下.env文件中的token与上面ws配置中相同即可，文件中没有则添加：
```bash
ONEBOT_ACCESS_TOKEN=12345ABCDE
```
