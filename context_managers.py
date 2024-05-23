from threading import Lock
from contextlib import contextmanager

lock = Lock()

with lock:
    for i in range(10):
        print("nothing to say")


@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todo...')

