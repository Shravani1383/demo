def sjf(processes, burst_times):
    n = len(processes)
    wt = [0] * n
    tat = [0] * n

    sorted_processes = sorted(range(n), key=lambda k: burst_times[k])

    for i in range(1, n):
        wt[sorted_processes[i]] = wt[sorted_processes[i - 1]] + burst_times[sorted_processes[i - 1]]

    for i in range(n):
        tat[i] = wt[i] + burst_times[i]

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n

    print("SJF Scheduling:")
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_times[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print("Average Waiting Time:", avg_wt)
    print("Average Turnaround Time:", avg_tat)

    return avg_wt


# Example usage:
if __name__ == "__main__":
    burst_time=[]
    process = []
    print("SJF algo")
    process_no= int(input("Enter No of process:"))
    for i in range(process_no):
        process.append(input(f"Enter process {i + 1}: "))
        burst_time.append(int(input("Enter process burst time")))

    sjf(process,burst_time)