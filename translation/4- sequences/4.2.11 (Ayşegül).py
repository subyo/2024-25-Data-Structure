def __contains__(self, item):
    for i in range(self.numItems):
        if self.items[i] == item:
            return True
    return False
