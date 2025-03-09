lst = [1, 2, 3]
lst2 = list("abc")
lst2
# ['a', 'b', 'c']
lst < lst2
# Traceback (most recent call last):
#   File "<string>", line 1, in <fragment>
# TypeError: unorderable types: int() < str()

lst3 = [4, 5, 6]
lst < lst3
# True

lst4 = [1, 3, 2]
lst < lst4
# True

lst5 = [1, 2, 2]
lst5 < lst
# True

lst6 = [1, 1, 'a']
lst6 < lst
# True
