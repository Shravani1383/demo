def calculate_times(processes, burst_times):
    n = len(processes)
    # Initialize lists to store finish time, turnaround time, and waiting time
    finish_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n

    # Calculate finish time for each process
    finish_times[0] = burst_times[0]
    for i in range(1, n):
        finish_times[i] = finish_times[i - 1] + burst_times[i]

    # Calculate turnaround time and waiting time for each process
    for i in range(n):
        turnaround_times[i] = finish_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    return finish_times, turnaround_times, waiting_times

def display_results(processes, finish_times, turnaround_times, waiting_times):
    print("Process\tBurst Time\tFinish Time\tTurnaround Time\tWaiting Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{burst_times[i]}\t\t{finish_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

if __name__ == "__main__":
    # Take user input for the number of processes
    n = int(input("Enter the number of processes: "))

    # Take user input for burst times of processes
    processes = []
    burst_times = []
    for i in range(n):
        processes.append(i + 1)
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        burst_times.append(burst_time)

    # Calculate times using FCFS algorithm
    finish_times, turnaround_times, waiting_times = calculate_times(processes, burst_times)

    # Display results
    display_results(processes, burst_times, finish_times, turnaround_times, waiting_times)