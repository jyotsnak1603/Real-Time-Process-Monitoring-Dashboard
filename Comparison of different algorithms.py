import time
import random

# Process structure
class Process:
    def __init__(self, pid, arrival_time, burst_time, deadline=None):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.deadline = deadline
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

# First Come First Serve (FCFS)
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    time_elapsed = 0
    for process in processes:
        if time_elapsed < process.arrival_time:
            time_elapsed = process.arrival_time
        process.waiting_time = time_elapsed - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        time_elapsed += process.burst_time

# Shortest Job Next (SJN)
def sjn_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    time_elapsed = 0
    ready_queue = []
    index = 0
    while index < len(processes) or ready_queue:
        while index < len(processes) and processes[index].arrival_time <= time_elapsed:
            ready_queue.append(processes[index])
            index += 1
        if ready_queue:
            ready_queue.sort(key=lambda x: x.burst_time)
            process = ready_queue.pop(0)
            process.waiting_time = time_elapsed - process.arrival_time
            process.turnaround_time = process.waiting_time + process.burst_time
            time_elapsed += process.burst_time
        else:
            time_elapsed = processes[index].arrival_time

# Round Robin (RR)
def rr_scheduling(processes, quantum=2):
    queue = processes[:]
    time_elapsed = 0
    while queue:
        process = queue.pop(0)
        if process.remaining_time > quantum:
            process.remaining_time -= quantum
            time_elapsed += quantum
            queue.append(process)
        else:
            time_elapsed += process.remaining_time
            process.remaining_time = 0
            process.turnaround_time = time_elapsed - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time

# Earliest Deadline First (EDF)
def edf_scheduling(processes):
    processes.sort(key=lambda x: (x.deadline, x.arrival_time))
    time_elapsed = 0
    for process in processes:
        if time_elapsed < process.arrival_time:
            time_elapsed = process.arrival_time
        process.waiting_time = time_elapsed - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        time_elapsed += process.burst_time

# Function to take user input for processes
def get_user_processes():
    processes = []
    num = int(input("Enter number of processes: "))
    for i in range(num):
        arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        deadline = int(input(f"Enter deadline for process {i+1} (if EDF is used): "))
        processes.append(Process(i+1, arrival_time, burst_time, deadline))
    return processes

# Function to calculate average waiting and turnaround time
def calculate_avg_times(processes):
    total_waiting = sum(p.waiting_time for p in processes)
    total_turnaround = sum(p.turnaround_time for p in processes)
    return total_waiting / len(processes), total_turnaround / len(processes)

# Running and comparing the algorithms
num_processes = 5
processes = get_user_processes()

# Run all scheduling algorithms
algorithms = {
    "FCFS": fcfs_scheduling,
    "SJN": sjn_scheduling,
    "Round Robin": lambda p: rr_scheduling(p, quantum=3),
    "EDF": edf_scheduling
}

results = {}
for name, algorithm in algorithms.items():
    proc_copy = [Process(p.pid, p.arrival_time, p.burst_time, p.deadline) for p in processes]
    algorithm(proc_copy)
    avg_wait, avg_turnaround = calculate_avg_times(proc_copy)
    results[name] = (avg_wait, avg_turnaround)

# Display comparison results
print("\nComparison of Scheduling Algorithms")
print("======================================")
for name, (avg_wait, avg_turnaround) in results.items():
    print(f"{name}: Avg Waiting Time = {avg_wait:.2f}, Avg Turnaround Time = {avg_turnaround:.2f}")
