'''
"status","network","netmask","nexthop","metric","locprf","weight","path","origin"
"*","1.0.0.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 15169","i"
"*>","1.0.0.0","24","200.219.145.23",NA,NA,0,"53242 7738 15169","i"
"*","1.0.4.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
"*>","1.0.4.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"
"*","1.0.5.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
'''
import asyncio
import aiofiles
import csv


async def do_nothing(n):
    for i in range(n):
        #print('do_nothing')
        await asyncio.sleep(0.1)


async def open_csv(filename):
    async with aiofiles.open(filename) as f:
        async for line in f:
            # make read slower
            #await asyncio.sleep(0.1)
            #print('open_csv')
            yield list(csv.reader([line]))[0]


async def filter_prefix_next_hop(iterable, nexthop):
    async for line in iterable:
        if line[3] == nexthop:
            yield line

async def get_n_lines(filename, n):
    data = open_csv(filename)
    nexthop_45 = filter_prefix_next_hop(data, "200.219.145.45")
    line = 0
    async for route in nexthop_45:
        print(route)
        line += 1
        if line == n:
            break


async def main():
    task1 = asyncio.create_task(do_nothing(10))
    task2 = asyncio.create_task(get_n_lines('rib.table.lg.ba.ptt.br-BGP.csv', 5))
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # asyncio.run(main())
    # при использовании asyncio.run появляется исключение, если генератор прерывается,
    # когда он не дошел до конца
    # пофиксили в последних версиях 3.7/3.8
    # https://bugs.python.org/issue38013
