import threading
import time
import random

class ReaderWriterProblem:
    def __init__(self):
        self.data = 0
        self.readers_count = 0
        self.readers_lock = threading.Lock()
        self.writers_lock = threading.Lock()

    def read(self, reader_id):
        with self.readers_lock:
            self.readers_count += 1
            if self.readers_count == 1:
                self.writers_lock.acquire()

        print(f"Reader {reader_id} is reading data: {self.data}")
        time.sleep(random.uniform(0, 1))

        with self.readers_lock:
            self.readers_count -= 1
            if self.readers_count == 0:
                self.writers_lock.release()

    def write(self, writer_id):
        with self.writers_lock:
            print(f"Writer {writer_id} is writing data")
            self.data += 1
            time.sleep(random.uniform(0, 1))

def reader_func(reader_id, rw_problem):
    for _ in range(5):
        rw_problem.read(reader_id)

def writer_func(writer_id, rw_problem):
    for _ in range(5):
        rw_problem.write(writer_id)

if __name__ == "__main__":
    rw_problem = ReaderWriterProblem()

    readers = [threading.Thread(target=reader_func, args=(i, rw_problem)) for i in range(3)]
    writers = [threading.Thread(target=writer_func, args=(i, rw_problem)) for i in range(2)]

    all_threads = readers + writers
    random.shuffle(all_threads)

    for thread in all_threads:
        thread.start()

    for thread in all_threads:
        thread.join()
