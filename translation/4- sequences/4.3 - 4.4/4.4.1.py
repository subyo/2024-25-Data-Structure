import turtle

class Point(turtle.RawTurtle):
    def __init__(self, canvas, x, y):
        super().__init__(canvas)
        canvas.register_shape("dot",((3,0),(2,2),(0,3),(-2,2),(-3,0),(-2,-2),(0,-3),(2,-2)))
        self.shape("dot")
        self.speed(200)
        self.penup()
        self.goto(x,y)
    def __str__(self):
        return "("+str(self.xcor())+","+str(self.ycor())+")"
    def __lt__(self, other):
        return self.ycor() < other.ycor()
screen = turtle.Screen()
draw = Point(screen, 100, 100)
print(draw)

turtle.done()