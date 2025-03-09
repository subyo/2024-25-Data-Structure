import copy

l = [0, 1, [2, 3]]
l_assign = l                   # assignment
l_copy = l.copy()              # shallow copy
l_deepcopy = copy.deepcopy(l)  # deep copy

l[1] = 100
l[2][0] = 200
print(l)
# [0, 100, [200, 3]]

print(l_assign)
# [0, 100, [200, 3]]

print(l_copy)
# [0, 1, [200, 3]]

print(l_deepcopy)
# [0, 1, [2, 3]]