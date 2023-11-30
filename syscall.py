import os
import platform

# Process-related system calls: fork, wait
def process_related_system_calls():
    if platform.system() == "Windows":
        print("Sorry, process-related system calls are not supported on Windows.")
        return

    pid = os.fork()

    if pid > 0:
        # Parent process
        print(f"Parent process (PID: {os.getpid()}), Child PID: {pid}")
        os.wait()  # Wait for the child process to finish
    elif pid == 0:
        # Child process
        print(f"Child process (PID: {os.getpid()})")
        # Child process execution
        os._exit(0)  # Terminate the child process

# File-related system calls: open, read, write, close
def file_related_system_calls():
    file_path = "example_file.txt"

    # Writing to a file
    with open(file_path, "w") as file:
        file.write("Hello, this is a sample file.\n")

    # Reading from a file
    with open(file_path, "r") as file:
        content = file.read()
        print(f"File content:\n{content}")

# Protection-related system call: chmod
def protection_related_system_call():
    file_path = "example_file.txt"

    # Changing file permissions
    os.chmod(file_path, 0o444)  # Give read-only permissions

    print("File permissions changed to read-only")

if __name__ == "__main__":
    # Process-related system calls
    print("Process-related system calls:")
    process_related_system_calls()

    # File-related system calls
    print("\nFile-related system calls:")
    file_related_system_calls()

    # Protection-related system call
    print("\nProtection-related system call:")
    protection_related_system_call()
