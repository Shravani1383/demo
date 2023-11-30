class PageReplacement:

    def __init__(self, reference_string, frame_size):
        self.reference_string = reference_string
        self.frame_size = frame_size
        self.frames = []
        self.page_faults = 0
                                             
    def fifo(self):
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

if __name__ == "__main__":
    reference_string = list(map(int, input("Enter the reference string (comma-separated numbers): ").split(',')))
    frame_size = int(input("Enter the frame size: "))
    # Create PageReplacement instance
    page_replacement = PageReplacement(reference_string, frame_size)
    # Use the FIFO algorithm
    faults = page_replacement.fifo()
    # Print the results
    print(f"FIFO Page Faults: {faults}")    