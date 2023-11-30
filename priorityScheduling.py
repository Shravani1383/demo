def priority_scheduling(processes, burst_times, priorities):
    n = len(processes)

    # Initialize lists to store finish time, turnaround time, and waiting time
    finish_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n

    # Create a list of tuples (process_id, burst_time, priority)
    process_info = list(zip(processes, burst_times, priorities))

    # Sort the processes based on priority (lower value means higher priority)
    process_info.sort(key=lambda x: x[2])

    # Calculate finish time for each process
    finish_times[0] = process_info[0][1]
    for i in range(1, n):
        finish_times[i] = finish_times[i - 1] + process_info[i][1]

    # Calculate turnaround time and waiting time for each process
    for i in range(n):
        turnaround_times[i] = finish_times[i]
        waiting_times[i] = turnaround_times[i] - process_info[i][1]

    return finish_times, turnaround_times, waiting_times

def display_results(processes, finish_times, turnaround_times, waiting_times):
    print("Process\tFinish Time\tTurnaround Time\tWaiting Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{finish_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

if __name__ == "__main__":
    # Take user input for the number of processes
    n = int(input("Enter the number of processes: "))

    # Take user input for burst times and priorities of processes
    processes = []
    burst_times = []
    priorities = []
    for i in range(n):
        processes.append(i + 1)
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        priority = int(input(f"Enter priority for Process {i + 1}: "))
        burst_times.append(burst_time)
        priorities.append(priority)

    # Calculate times using Priority Scheduling algorithm
    finish_times, turnaround_times, waiting_times = priority_scheduling(processes, burst_times, priorities)

    # Display results
    display_results(processes, finish_times, turnaround_times, waiting_times)


