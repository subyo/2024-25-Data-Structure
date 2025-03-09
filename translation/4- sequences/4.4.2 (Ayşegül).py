def main():
    t = turtle.Turtle()
    t.ht()
    screen = t.getscreen()
    lst = []
    for i in range(10):
        for j in range(10):
            pair = Point(screen, i, j)
            lst.append(pair)
    lst.sort()
    for p in lst:
        print(p)
