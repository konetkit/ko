import typer

app = typer.Typer()

from ko.commands.ping.extlib import ping as ping_extlib
from ko.commands.ping.mycode import ping as ping_mycode
from ko.commands.ping.system import ping as ping_system

@app.command()
def ping(host: str,
        mode: str = typer.Option("system", help="extlib | mycode | system")):
    if mode == "system":
        ping_system(host)
    elif mode == "extlib":
        ping_extlib(host)
    elif mode == "mycode":
        ping_mycode(host)
    else:
        typer.echo("Chế độ không hợp lệ")

@app.command()
def noop():
    pass

if __name__ == "__main__":
    app()
