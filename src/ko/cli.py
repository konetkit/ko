import typer

app = typer.Typer()


from ko.commands.telnet.extlib import telnet as telnet_extlib
from ko.commands.telnet.extlib_legacy import telnet as telnet_extlib_legacy
from ko.commands.telnet.mycode import telnet as telnet_mycode
from ko.commands.telnet.system import telnet as telnet_system

@app.command()
def telnet(host: str, port: int = 23, mode: str = "system", legacy: bool = False):
    if mode == "system":
        telnet_system(host, port)
    elif mode == "extlib":
        if legacy:
            telnet_extlib_legacy(host, port)
        else:
            telnet_extlib(host, port)
    elif mode == "legacy":
        telnet_legacy_extlib(host, port)
    elif mode == "mycode":
        telnet_mycode(host, port)
    else:
        typer.echo(f"Unknown mode: {mode}")


from ko.commands.ncat.cli import app as sub_ncat
app.add_typer(sub_ncat)

from ko.commands.ping.cli import app as sub_ping
app.add_typer(sub_ping)

@app.command()
def noop():
    pass

if __name__ == "__main__":
    app()
