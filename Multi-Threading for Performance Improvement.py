import time
import psutil
import threading

def monitor_cpu():
    while True:
        print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
        time.sleep(2)

def monitor_memory():
    while True:
        mem = psutil.virtual_memory()
        print(f"Total RAM: {mem.total // (1024 * 1024)} MB, Free RAM: {mem.available // (1024 * 1024)} MB")
        time.sleep(2)

cpu_thread = threading.Thread(target=monitor_cpu)
ram_thread = threading.Thread(target=monitor_memory)

cpu_thread.start()
ram_thread.start()
