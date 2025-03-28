import time
import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem_info = psutil.virtual_memory()
    return mem_info.total // (1024 * 1024), mem_info.available // (1024 * 1024)

def main():
    while True:
        cpu_usage = get_cpu_usage()
        total_ram, free_ram = get_memory_usage()

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Total RAM: {total_ram} MB, Free RAM: {free_ram} MB")
        time.sleep(2)

if __name__ == "__main__":
    main()
