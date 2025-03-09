def __repr__(self):
    s = "PyList(["
    for i in range(self.numItems):
        s = s + repr(self.items[i])
        if i < self.numItems - 1:
            s = s + ", "
    s = s + "])"
    return s
