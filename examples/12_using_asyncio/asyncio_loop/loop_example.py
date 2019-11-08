from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import netdev


async def connect_ssh(device, command):
    print(f'Подключаюсь к {device["host"]}')
    try:
        async with netdev.create(**device) as ssh:
            await asyncio.sleep(10)
            output = await ssh.send_command(command)
        return output
    except asyncio.CancelledError as e:
        print('Отмена операции {device["host"]}')


async def send_command_to_devices(devices, command):
    try:
        coroutines = map(connect_ssh, devices, repeat(command))
        result = await asyncio.gather(*coroutines)
        return result
    except asyncio.CancelledError as e:
        print('Отмена операции')


def main():
    with open('devices_netmiko.yaml') as f:
        devices = yaml.safe_load(f)

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(send_command_to_devices(devices, 'sh clock'))
    loop.close()
    print(result)


if __name__ == "__main__":
    main()
