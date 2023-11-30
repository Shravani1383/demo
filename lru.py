from collections import deque

class PageReplacement:
    def __init__(self, reference_string, frame_size):
        self.reference_string = reference_string
        self.frame_size = frame_size
        self.frames = deque(maxlen=frame_size)
        self.page_faults = 0

    def lru(self):
        for page in self.reference_string:
            if page not in self.frames:
                self.page_faults += 1
                if len(self.frames) < self.frame_size:
                    self.frames.append(page)
                else:
                    # Remove the least recently used page from the left
                    self.frames.popleft()
                    self.frames.append(page)
            else:
                # Move the page to the most recently used position
                self.frames.remove(page)
                self.frames.append(page)
        return self.page_faults

if __name__ == "__main__":
    try:
        reference_string = list(map(int, input("Enter the reference string (comma-separated numbers): ").split(',')))
        frame_size = int(input("Enter the frame size: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        exit()

    page_replacement = PageReplacement(reference_string, frame_size)
    faults = page_replacement.lru()
    print(f"LRU Page Faults: {faults}")
