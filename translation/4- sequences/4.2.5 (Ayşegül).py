# This method is hidden since it starts with two underscores.
# It is only available to the class to use.
def __makeroom(self):
    # Increase list size by 1/4 to make more room.
    # Add one in case for some reason self.size is 0.
    newlen = (self.size // 4) + self.size + 1
    newlst = [None] * newlen
    for i in range(self.numItems):
        newlst[i] = self.items[i]
    self.items = newlst
    self.size = newlen

def append(self, item):
    if self.numItems == self.size:
        self.__makeroom()
    self.items[self.numItems] = item
    self.numItems += 1  # Same as writing self.numItems = self.numItems + 1
