from pprint import pprint
import asyncio
from itertools import repeat
from random import random

import yaml
import netdev


async def connect_ssh(device, command):
    print(f'>>> Подключаюсь к {device["host"]}')
    try:
        async with netdev.create(**device) as ssh:
            await asyncio.sleep(random()*10)
            output = await ssh.send_command(command)
            print(f'<<< Получен результат от {device["host"]}')
        return output
    except asyncio.CancelledError as e:
        print(f'Отмена операции {device["host"]}')


async def send_command_to_devices(devices, command):
    try:
        coroutines = map(connect_ssh_with_semaphore, devices, repeat(command))
        #coroutines = map(connect_ssh, devices, repeat(command))
        result = await asyncio.gather(*coroutines)
        return result
    except asyncio.CancelledError as e:
        print('Отмена операции')


semaphore = asyncio.Semaphore(2)

async def connect_ssh_with_semaphore(*args, **kwargs):
    async with semaphore:
        return await connect_ssh(*args, **kwargs)


def main():
    with open('devices_netmiko.yaml') as f:
        devices = yaml.safe_load(f)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(send_command_to_devices(devices, 'sh clock'))
    finally:
        loop.close()


if __name__ == "__main__":
    main()
