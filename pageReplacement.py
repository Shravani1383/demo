class PageReplacement:
    def __init__(self, reference_string, frame_size):
        self.reference_string = reference_string
        self.frame_size = frame_size
        self.frames = []
        self.page_faults = 0

    def reset_frames(self):
        self.frames = []
        self.page_faults = 0

    def fifo(self):
        self.reset_frames()
        for page in self.reference_string:
            if page not in self.frames:
                if len(self.frames) < self.frame_size:
                    self.frames.append(page)
                else:
                    self.frames.pop(0)
                    self.frames.append(page)
                self.page_faults += 1
            else:
                pass  # Page is already in the frame
        return self.page_faults

    def lru(self):
        self.reset_frames()
        for page in self.reference_string:
            if page not in self.frames:
                if len(self.frames) < self.frame_size:
                    self.frames.append(page)
                else:
                    # Find the least recently used page and replace it
                    index = min(range(len(self.frames)), key=self.frames.__getitem__)
                    self.frames[index] = page
                self.page_faults += 1
            else:
                # Move the used page to the end to mark it as most recently used
                self.frames.remove(page)
                self.frames.append(page)
        return self.page_faults

    def optimal(self):
        self.reset_frames()
        for i, page in enumerate(self.reference_string):
            if page not in self.frames:
                if len(self.frames) < self.frame_size:
                    self.frames.append(page)
                else:
                    # Find the page that will not be used for the longest time in the future
                    future_pages = self.reference_string[i+1:]
                    future_occurrences = {p: future_pages.index(p) if p in future_pages else float('inf') for p in self.frames}
                    page_to_replace = max(future_occurrences, key=future_occurrences.get)
                    self.frames[self.frames.index(page_to_replace)] = page
                self.page_faults += 1
            else:
                pass  # Page is already in the frame
        return self.page_faults

def get_user_input():
    reference_string = list(map(int, input("Enter the reference string (comma-separated numbers): ").split(',')))
    frame_size = int(input("Enter the frame size: "))
    return reference_string, frame_size

# Example usage:
if __name__ == "__main__":
    reference_string, frame_size = get_user_input()

    page_replacement = PageReplacement(reference_string, frame_size)

    algorithm_choice = input("Choose a page replacement algorithm (FIFO, LRU, Optimal): ").lower()

    if algorithm_choice == 'fifo':
        faults = page_replacement.fifo()
    elif algorithm_choice == 'lru':
        faults = page_replacement.lru()
    elif algorithm_choice == 'optimal':
        faults = page_replacement.optimal()
    else:
        print("Invalid choice. Please choose from FIFO, LRU, or Optimal.")
        faults = 0

    print(f"{algorithm_choice} Page Faults: {faults}")
