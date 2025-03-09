def insert(self, i, e):
    if self.numItems == self.size:
        self.__makeroom()
    if i < self.numItems:
        for j in range(self.numItems - 1, i - 1, -1):
            self.items[j + 1] = self.items[j]
        self.items[i] = e
        self.numItems += 1
    else:
        self.append(e)
