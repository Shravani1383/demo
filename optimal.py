class PageReplacement:
    def __init__(self, reference_string, frame_size):
        self.reference_string = reference_string
        self.frame_size = frame_size
        self.frames = []
        self.page_faults = 0
            
    def optimal(self):
        self.frames = []  # Reset frames at the beginning of each run
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

if __name__ == "__main__":
    try:
        reference_string = list(map(int, input("Enter the reference string (comma-separated numbers): ").split(',')))
        frame_size = int(input("Enter the frame size: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        exit()

    page_replacement = PageReplacement(reference_string, frame_size)
    faults = page_replacement.optimal()
    print(f"Optimal Page Faults: {faults}")

