import asyncio
import aioconsole
import telnetlib3

def telnet(host, port):
    try:
        asyncio.run(telnet_main(host, port))
    except KeyboardInterrupt:
        print("\nDisconnected.")
    except Exception as e:
        print(f"Error: {e}")

async def telnet_main(host, port):
    reader, writer = await telnetlib3.open_connection(host, port)
    print(f"Trying {host}...\nConnected to {host}.\nEscape character is '^]'.")
    await interact(reader, writer)
    return (reader, writer)

async def interact(reader, writer):
    async def read_from_server():
        while True:
            data = await reader.read(1024)
            if not data:
                break
            print(data, end='', flush=True)

    async def read_from_input():
        while True:
            line = await aioconsole.ainput()
            if not line:
                break
            writer.write(line.rstrip('\r\n') + '\r\n')

    await asyncio.gather(read_from_server(), read_from_input())
