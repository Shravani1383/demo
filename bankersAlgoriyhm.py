import numpy as np

def find_safe_sequence(available, max_claim, allocation):
    processes = len(max_claim)
    safe_sequence = []
    work = available.copy()
    finish = [False] * processes

    while True:
        found = False
        for i in range(processes):
            if not finish[i] and all(need <= work for need, work in zip(max_claim[i], work)):
                # Process i can finish
                finish[i] = True
                work = np.add(work, allocation[i])
                safe_sequence.append(i)
                found = True

        if not found:
            break

    if all(finish):
        return safe_sequence
    else:
        return []

def bankers_algorithm():
    # Get user input
    processes = int(input("Enter the number of processes: "))
    resources = int(input("Enter the number of resources: "))

    # Maximum resource claim matrix
    max_claim = np.zeros((processes, resources), dtype=int)
    for i in range(processes):
        max_claim[i] = list(map(int, input(f"Enter maximum resource claim for process {i + 1} (space-separated): ").split()))

    # Current allocation matrix
    allocation = np.zeros((processes, resources), dtype=int)
    for i in range(processes):
        allocation[i] = list(map(int, input(f"Enter current allocation for process {i + 1} (space-separated): ").split()))

    # Available resources vector
    available = np.array(list(map(int, input("Enter available resources (space-separated): ").split())))

    # Find a safe sequence
    safe_sequence = find_safe_sequence(available, max_claim, allocation)

    if safe_sequence:
        print("The system is in a safe state.")
        print("Safe Sequence:", safe_sequence)
    else:
        print("The system is NOT in a safe state.")

if __name__ == "__main__":
    bankers_algorithm()
