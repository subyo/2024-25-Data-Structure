def __add__(self, other):
    result = PyList(size=self.numItems + other.numItems)
    for i in range(self.numItems):
        result.append(self.items[i])
    for i in range(other.numItems):
        result.append(other.items[i])
    return result
