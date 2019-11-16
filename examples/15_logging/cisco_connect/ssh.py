import netmiko
import logging

logger = logging.getLogger(__name__)

print('Import cisco_connect/ssh.py')
print("__name__:", __name__)

class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def send_show_command(self, command):
        output = self.ssh.send_command(command)
        logger.debug(output)
        return output

