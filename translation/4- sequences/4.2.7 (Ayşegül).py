def __delitem__(self, index):
    for i in range(index, self.numItems - 1):
        self.items[i] = self.items[i + 1]
    self.numItems -= 1  # Same as writing self.numItems = self.numItems - 1
