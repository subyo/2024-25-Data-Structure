def __iter__(self):
    for i in range(self.numItems):
        yield self.items[i]
