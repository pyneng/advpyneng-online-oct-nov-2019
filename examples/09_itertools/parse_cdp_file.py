import re
from pprint import pprint
from itertools import dropwhile, takewhile


def get_cdp_neighbor(sh_cdp_neighbor_detail):
    with open(sh_cdp_neighbor_detail) as f:
        while True:
            f = dropwhile(lambda x: not 'Device ID' in x, f)
            lines = takewhile(lambda y: not '-----' in y, f)
            neighbor = ''.join(lines)
            if not neighbor:
                return None
            yield neighbor


def parse_cdp_neighbor(output):
    regex = ('Device ID: (\S+)\n.*?'
             ' +IP address: (?P<ip>\S+).+?'
             'Platform: (?P<platform>\S+ \S+),.+?'
             'Version (?P<ios>\S+),')

    result = {}
    match = re.search(regex, output, re.DOTALL)
    if match:
        device = match.group(1)
        result[device] = match.groupdict()
    return result


def parse_cdp_output(filename):
    result = get_cdp_neighbor(filename)
    all_cdp = {}
    for neighbor in result:
        all_cdp.update(parse_cdp_neighbor(neighbor))
    return all_cdp


if __name__ == "__main__":
    filename = 'sh_cdp_neighbors_detail.txt'
    pprint(parse_cdp_output(filename), width=120)
