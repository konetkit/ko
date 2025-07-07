import typer
import sys

app = typer.Typer()

@app.command("ncat")
def run(
    host: str = typer.Argument(None),
    port: int = typer.Option(None, "--port", "-p"),
    listen: bool = typer.Option(False, "--listen", "-l"),
    mode: str = typer.Option("system", help="Mode: mycode, system"),
):
    """
    Netcat-like utility: client or server.
    """
    if mode == "system":
        from ko.commands.ncat.system import ncat as runner
    elif mode == "mycode":
        from ko.commands.ncat.mycode import ncat as runner
    else:
        print(f"Unknown mode: {mode}")
        raise typer.Exit(1)

    if listen:
        runner(host="0.0.0.0", port=port, listen=True)
    else:
        if not host or not port:
            print("Client mode requires host and port.")
            raise typer.Exit(1)
        runner(host=host, port=port, listen=False)
