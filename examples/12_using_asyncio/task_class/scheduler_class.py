class Scheduler:
    def __init__(self):
        self.tasks = deque()
        self.done = {}
        self.failed = {}

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        while len(self.tasks) != 0:
            task = self.tasks.popleft()
            print('Running task...')
            try:
                task._step()
            except StopIteration as e:
                print('Task completed')
                self.done[task.name] = e.value
            except Exception as e:
                self.failed[task.name] = e
            else:
                self.tasks.append(task)



s = Scheduler()

