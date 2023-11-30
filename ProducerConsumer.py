import threading
import time
import random

class ProducerConsumerProblem:
    def __init__(self, buffer_size):
        self.buffer = []
        self.buffer_size = buffer_size
        self.mutex = threading.Lock()
        self.empty = threading.Semaphore(buffer_size)
        self.full = threading.Semaphore(0)

    def produce_item(self, producer_id):
        item = random.randint(1, 100)
        self.empty.acquire()  # Wait if the buffer is full
        self.mutex.acquire()  # Enter critical section
        self.buffer.append(item)
        print(f"Producer {producer_id} produced item: {item}")
        self.mutex.release()  # Exit critical section
        self.full.release()   # Signal that the buffer is not empty

    def consume_item(self, consumer_id):
        self.full.acquire()   # Wait if the buffer is empty
        self.mutex.acquire()  # Enter critical section
        item = self.buffer.pop(0)
        print(f"Consumer {consumer_id} consumed item: {item}")
        self.mutex.release()  # Exit critical section
        self.empty.release()  # Signal that the buffer is not full

def producer_thread(producer_id, pc_problem):
    for _ in range(5):  # Produce 5 items
        pc_problem.produce_item(producer_id)
        time.sleep(random.uniform(0, 1))

def consumer_thread(consumer_id, pc_problem):
    for _ in range(5):  # Consume 5 items
        pc_problem.consume_item(consumer_id)
        time.sleep(random.uniform(0, 1))

if __name__ == "__main__":
    pc_problem = ProducerConsumerProblem(buffer_size=3)

    # Create producer threads
    producers = [threading.Thread(target=producer_thread, args=(i, pc_problem)) for i in range(2)]

    # Create consumer threads
    consumers = [threading.Thread(target=consumer_thread, args=(i, pc_problem)) for i in range(3)]

    # Start all threads
    for producer in producers:
        producer.start()

    for consumer in consumers:
        consumer.start()

    # Wait for all threads to finish
    for producer in producers:
        producer.join()

    for consumer in consumers:
        consumer.join()