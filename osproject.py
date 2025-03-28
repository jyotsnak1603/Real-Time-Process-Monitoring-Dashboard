import os
import time
import psutil
import keyboard

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get Memory usage
def get_memory_usage():
    mem_info = psutil.virtual_memory()
    total_ram = mem_info.total // (1024 * 1024)  # Convert bytes to MB
    free_ram = mem_info.available // (1024 * 1024)  # Convert bytes to MB
    print(f"Total RAM: {total_ram} MB")
    print(f"Free RAM: {free_ram} MB")

# Function to simulate Earliest Deadline First (EDF) scheduling algorithm
def earliest_deadline_first():
    print("Simulating Earliest Deadline First (EDF) Scheduling...")

# Function to simulate another scheduling algorithm for comparison
def different_algorithm_comparison():
    print("Comparing with another scheduling algorithm...")

# Main loop to monitor CPU and memory usage
cpu_usages = []
max_samples = 10

try:
    while True:
        os.system("cls")  # Clear screen for Windows
        cpu_usage = get_cpu_usage()
        print(f"CPU Usage: {cpu_usage}%")
        get_memory_usage()

        cpu_usages.append(cpu_usage)
        if len(cpu_usages) > max_samples:
            cpu_usages.pop(0)

        avg_cpu = sum(cpu_usages) / len(cpu_usages)
        print(f"Average CPU Usage (Last {len(cpu_usages)} readings): {avg_cpu}%")

        # Perform EDF scheduling and comparison
        earliest_deadline_first()
        different_algorithm_comparison()

        print("\nPress 'q' to stop monitoring...")

        # Check if 'q' is pressed
        if keyboard.is_pressed("q"):
            print("\nStopping Monitoring...\n")
            break

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
