import matplotlib.pyplot as plt
import seaborn as sns

def get_user_input():
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        pid = input(f"Enter Process ID for process {i+1}: ")
        arrival_time = int(input(f"Enter Arrival Time for {pid}: "))
        burst_time = int(input(f"Enter Burst Time for {pid}: "))
        deadline = int(input(f"Enter Deadline for {pid} (only for EDF): "))
        processes.append((pid, arrival_time, burst_time, deadline))
    return processes

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    start_time, completion_time, turnaround_time, waiting_time = {}, {}, {}, {}
    current_time = 0

    for process in processes:
        pid, arrival, burst, _ = process
        if current_time < arrival:
            current_time = arrival
        start_time[pid] = current_time
        completion_time[pid] = current_time + burst
        turnaround_time[pid] = completion_time[pid] - arrival
        waiting_time[pid] = turnaround_time[pid] - burst
        current_time += burst

    return start_time, completion_time, turnaround_time, waiting_time

def edf_scheduling(processes):
    processes.sort(key=lambda x: x[3])  # Sort by deadline
    start_time, completion_time, turnaround_time, waiting_time = {}, {}, {}, {}
    current_time = 0

    for process in processes:
        pid, arrival, burst, deadline = process
        if current_time < arrival:
            current_time = arrival
        start_time[pid] = current_time
        completion_time[pid] = current_time + burst
        turnaround_time[pid] = completion_time[pid] - arrival
        waiting_time[pid] = turnaround_time[pid] - burst
        current_time += burst

    return start_time, completion_time, turnaround_time, waiting_time

def plot_scheduling_results(fcfs_times, edf_times, processes):
    pids = [p[0] for p in processes]
    
    plt.figure(figsize=(10, 5))
    sns.barplot(x=pids, y=[fcfs_times[2][p] for p in pids], color='blue', label='FCFS Turnaround Time')
    sns.barplot(x=pids, y=[edf_times[2][p] for p in pids], color='orange', alpha=0.7, label='EDF Turnaround Time')
    plt.xlabel("Processes")
    plt.ylabel("Turnaround Time")
    plt.title("Comparison of Turnaround Time in FCFS vs EDF")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    processes = get_user_input()
    fcfs_results = fcfs_scheduling(processes)
    edf_results = edf_scheduling(processes)
    
    print("\nFCFS Scheduling Results:")
    print("PID\tStart Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for pid in fcfs_results[0]:
        print(f"{pid}\t{fcfs_results[0][pid]}\t{fcfs_results[1][pid]}\t{fcfs_results[2][pid]}\t{fcfs_results[3][pid]}")
    
    print("\nEDF Scheduling Results:")
    print("PID\tStart Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for pid in edf_results[0]:
        print(f"{pid}\t{edf_results[0][pid]}\t{edf_results[1][pid]}\t{edf_results[2][pid]}\t{edf_results[3][pid]}")
    
    plot_scheduling_results(fcfs_results, edf_results, processes)
