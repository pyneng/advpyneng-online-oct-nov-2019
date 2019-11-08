import asyncio


async def ping(ip):
    reply = await asyncio.create_subprocess_shell(
        f'ping -c 3 -n {ip}',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await reply.communicate()

    ip_is_reachable = reply.returncode == 0
    return ip_is_reachable


if __name__ == "__main__":
    asyncio.run(ping('8.8.8.8'))
