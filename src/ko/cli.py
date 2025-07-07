import typer

app = typer.Typer()


from ko.commands.ncat.cli import app as sub_ncat
app.add_typer(sub_ncat)

from ko.commands.ping.cli import app as sub_ping
app.add_typer(sub_ping)

from ko.commands.telnet.cli import app as sub_telnet
app.add_typer(sub_telnet)


if __name__ == "__main__":
    app()
