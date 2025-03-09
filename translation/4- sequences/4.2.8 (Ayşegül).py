def __eq__(self, other):
    if type(other) != type(self):
        return False
    if self.numItems != other.numItems:
        return False
    for i in range(self.numItems):
        if self.items[i] != other.items[i]:
            return False
    return True
