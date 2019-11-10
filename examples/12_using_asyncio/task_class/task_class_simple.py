import weakref
import asyncio
Future = asyncio.futures.Future

# WeakSet containing all alive tasks.
_all_tasks = weakref.WeakSet()


def _register_task(task):
    """Register a new task in asyncio as executed by loop."""
    _all_tasks.add(task)


class Task(Future):
    """Simple prototype of Task"""

    def __init__(self, coro, *, loop=None, name=None):
        self.name = name
        print(f'Task {self.name} __init__')
        super().__init__(loop=loop)
        self._coro = coro
        self._loop.call_soon(self.__step)
        _register_task(self)

    def __step(self, val=None, exc=None):
        print(f'Task {self.name} __step')
        try:
            if exc:
                f = self._coro.throw(exc)
            else:
                f = self._coro.send(val)
        except StopIteration as e:
            self.set_result(e.value)
        except Exception as e:
            self.set_exception(e)
        else:
            f.add_done_callback(
                 self._wakeup)

    def _wakeup(self, fut):
        print(f'Task {self.name} _wakeup')
        try:
            res = fut.result()
        except Exception as e:
            self.__step(None, e)
        else:
            self.__step(res, None)

async def coro1():
    print("Start")
    await Task(asyncio.sleep(3), name='sleep coro1')
    print("Working")
    await asyncio.sleep(1)
    print("End")


async def coro2():
    await Task(asyncio.sleep(3), name='sleep coro2')
    print("Hello Bar")


async def main():
    task1 = Task(coro1(), name='coro1')
    #task2 = Task(coro2(), name='coro2')
    await asyncio.gather(task1)

asyncio.run(main())
