import typer

app = typer.Typer()

from .extlib import telnet as telnet_extlib
from .extlib_legacy import telnet as telnet_extlib_legacy
from .mycode import telnet as telnet_mycode
from .system import telnet as telnet_system

@app.command()
def telnet(host: str, port: int = 23, mode: str = "system", legacy: bool = False):
    if mode == "system":
        telnet_system(host, port)
    elif mode == "extlib":
        if legacy:
            telnet_extlib_legacy(host, port)
        else:
            telnet_extlib(host, port)
    elif mode == "mycode":
        telnet_mycode(host, port)
    else:
        typer.echo(f"Unknown mode: {mode}")
