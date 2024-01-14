import random
import socket
import uvicorn
import webview
import threading
from backend.app import app


def get_unused_port():
    """获取未被使用的端口"""
    while True:
        port = random.randint(1024, 65535)  # 端口范围一般为1024-65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(("127.0.0.1", port))
            sock.close()
            return port
        except OSError:
            pass


port = get_unused_port()

# 启动FastAPI服务
t = threading.Thread(target=uvicorn.run, args=(app,), kwargs={"host":"0.0.0.0", "port": port})
t.daemon = True
t.start()

# 在PyWebview应用程序中加载FastAPI应用程序的URL
webview.create_window('FastAPI Desktop', f'http://127.0.0.1:{port}/index.html')
webview.start()