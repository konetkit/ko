import typer

app = typer.Typer()

from .extlib import ping as ping_extlib
from .mycode import ping as ping_mycode
from .system import ping as ping_system

@app.command("ping")
def ping(host: str,
        mode: str = typer.Option("system", help="extlib | mycode | system")):
    if mode == "system":
        ping_system(host)
    elif mode == "extlib":
        ping_extlib(host)
    elif mode == "mycode":
        ping_mycode(host)
    else:
        typer.echo(f"Unknown mode: {mode}")
