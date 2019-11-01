from pprint import pprint
import asyncio
from itertools import repeat

import asyncssh


async def connect_ssh(ip, command, username='cisco', password='cisco'):
    print(f'Подключаюсь к {ip}')
    async with asyncssh.connect(ip, username=username, password=password) as ssh:
        print(f'Отправляю команду {command} на устройство {ip}')
        result = await ssh.run(command)
    return result.stdout


async def send_command_to_devices(ip_list, command):
    coroutines = map(connect_ssh, ip_list, repeat(command))
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    ip_list = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
    result = asyncio.run(send_command_to_devices(ip_list, 'sh clock'))
    pprint(result)

