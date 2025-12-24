import time
from concurrent.futures import ThreadPoolExecutor

def task(n):
    time.sleep(1)  # simulate I/O work
    print(f"Processing {n}")

with ThreadPoolExecutor(max_workers=3) as pool:
    pool.map(task, [1, 2, 3, 4])

