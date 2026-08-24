# 需要的库：
```bash
pip install nb-cli  nonebot2[fastapi] nonebot-adapter-onebot openai mcstatus
pip install nonebot_plugin_emojimix
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
        "token": "xxxx",
        "debug": false,
        "heartInterval": 30000
      }
```

nonebot中配置的token在nonebot路径下.env，没有则添加：
```bash
ONEBOT_ACCESS_TOKEN=xxxx（应该可以随便填）
```
