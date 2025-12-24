import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def task(n):
    # Simulate some work
    time.sleep(1)  
    print(f"Processing {n}")
    return n * 2  # just an example return value

# Create a thread pool with 3 workers
with ThreadPoolExecutor(max_workers=3) as pool:
    # Submit tasks individually
    futures = [pool.submit(task, n) for n in [1, 2, 3, 4, 5]]

    # Process results as they complete (order may be different from submission)
    for future in as_completed(futures):
        result = future.result()
        print(f"Result: {result}")

