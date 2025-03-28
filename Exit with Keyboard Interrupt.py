import time
import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem_info = psutil.virtual_memory()
    return mem_info.total // (1024 * 1024), mem_info.available // (1024 * 1024)

def earliest_deadline_first():
    print("Simulating EDF Scheduling...")

def main():
    cpu_usages = []
    max_samples = 5  

    try:
        while True:
            cpu_usage = get_cpu_usage()
            total_ram, free_ram = get_memory_usage()

            cpu_usages.append(cpu_usage)
            if len(cpu_usages) > max_samples:
                cpu_usages.pop(0)

            avg_cpu = sum(cpu_usages) / len(cpu_usages)

            print(f"CPU Usage: {cpu_usage}% (Avg: {avg_cpu:.2f}%)")
            print(f"Total RAM: {total_ram} MB, Free RAM: {free_ram} MB")

            earliest_deadline_first()

            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
