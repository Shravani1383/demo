def round_robin(processes, burst_times, time_quantum):
    n = len(processes)

    # Initialize lists to store finish time, turnaround time, and waiting time
    finish_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n

    # Create a copy of burst times to keep track of remaining burst times
    remaining_burst_times = burst_times.copy()

    # Initialize variables
    time = 0
    index = 0

    # Continue processing until all processes are done
    while any(remaining_burst_times):
        # Process each process in a round-robin manner
        for i in range(n):
            if remaining_burst_times[i] > 0:
                if remaining_burst_times[i] <= time_quantum:
                    # Process completes within the time quantum
                    time += remaining_burst_times[i]
                    finish_times[i] = time
                    turnaround_times[i] = finish_times[i]
                    waiting_times[i] = turnaround_times[i] - burst_times[i]
                    remaining_burst_times[i] = 0
                else:
                    # Process needs more time, deduct time quantum
                    time += time_quantum
                    remaining_burst_times[i] -= time_quantum

    return finish_times, turnaround_times, waiting_times

def display_results(processes, finish_times, turnaround_times, waiting_times):
    print("Process\tFinish Time\tTurnaround Time\tWaiting Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{finish_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

if __name__ == "__main__":
    # Take user input for the number of processes and time quantum
    n = int(input("Enter the number of processes: "))
    time_quantum = int(input("Enter the time quantum: "))

    # Take user input for burst times of processes
    processes = []
    burst_times = []
    for i in range(n):
        processes.append(i + 1)
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        burst_times.append(burst_time)

    # Calculate times using Round Robin algorithm
    finish_times, turnaround_times, waiting_times = round_robin(processes, burst_times, time_quantum)

    # Display results
    display_results(processes, finish_times, turnaround_times, waiting_times)
