def __getitem__(self, index):
    if 0 <= index < self.numItems:
        return self.items[index]
    raise IndexError("PyList index out of range")

def __setitem__(self, index, val):
    if 0 <= index < self.numItems:
        self.items[index] = val
        return
    raise IndexError("PyList assignment index out of range")
