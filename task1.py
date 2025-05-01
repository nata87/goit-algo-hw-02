from queue import Queue
import time

queue = Queue()
request_id = 1

def generate_request():
    global request_id
    request = f"Request #{request_id}"
    print(f"Створено: {request}")
    queue.put(request)
    request_id += 1

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Оброблено: {request}")
    else:
        print("Черга пуста, нема що обробляти")


for _ in range(5):
    generate_request()
    time.sleep(1)

for _ in range(6):  
    process_request()
    time.sleep(1)
