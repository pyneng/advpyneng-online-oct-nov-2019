# https://pyneng2.readthedocs.io/en/latest/book/02_oop_special_methods/add_method.html
import yaml
import sys
from netmiko import ConnectHandler, NetMikoAuthenticationException
import ipaddress

### example 1

class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return f"IPAddress: {self.ip}"

    def __repr__(self):
        return f"IPAddress('{self.ip}')"

    def __add__(self, other):
        result = self.ip + other
        return IPAddress(result)

### example 2

class IPv4Network:
    def __init__(self, network):
        self._net = ipaddress.ip_network(network)
        self.address = str(self._net.network_address)
        self.mask = self._net.prefixlen
        self.allocated = tuple()

    def hosts(self):
        return tuple([str(ip) for ip in self._net.hosts()])

    def allocate(self, ip):
        self.allocated += (ip,)

    def unassigned(self):
        return tuple([ip for ip in self.hosts() if ip not in self.allocated])

### example 3 key type

class Topology():
    def __init__(self, topology_dict):
        self.topology = topology_dict.copy()

    def __getitem__(self, item):
        return self.topology[item]

### example 4 optional
def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except NetMikoAuthenticationException as error:
        print(error)
        return None

def main(devices_filename, command):
    with open(devices_filename) as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        hostname = dev['host']
        output = send_show_command(dev, command)
        result = hostname + output
        print(result)
