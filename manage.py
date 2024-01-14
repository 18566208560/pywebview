import os
import sys
import typer
import uvicorn
from PyInstaller import __main__ as pyi

main = typer.Typer()

CUR_PATH = os.path.dirname(os.path.abspath(__file__))


@main.command()
def start(reload: bool = typer.Option(False, "--reload", "-r", help="auto reload"),
          port: int = typer.Option(8000, "--port", "-p", help="workers"),
          workers: int = typer.Option(1, "--workers", "-w", help="workers")):
    from backend.app import app
    uvicorn.run(app, host="0.0.0.0", port=port, reload=reload, workers=workers)

@main.command()
def build():
    os.chdir(os.path.join(CUR_PATH, "front"))
    os.system("npm run build")
    os.chdir(CUR_PATH)
    if not os.path.exists("./main.spec"):
        pyi.run(["-F", '--add-data', 'public:public', "main.py"])
    pyi.run(['main.spec'])

if __name__ == "__main__":
    main()
