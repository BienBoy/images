import sys
from pathlib import Path

src = Path(__file__).resolve().parent / 'src'
if str(src) not in sys.path:
    sys.path.insert(0, str(src))

from core.config import load_config
from core.runner import Runner
from core.scheduler import Scheduler
from core.storage import Storage


config = load_config('config/tasks.yaml')
storage = Storage()
scheduler = Scheduler(storage, None)

for task in config['tasks']:
    if task['name'] not in ['HDU', 'Anisaga', 'TTG', 'HDDolby']:
        # task['params']['headless'] = False
        Runner(scheduler.scheduler, storage, None).run_task(task)
