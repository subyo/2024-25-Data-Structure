#TheConnectFourFront-End
import turtle
import subprocess
import tkinter
import sys
import time

# The following program will play connect four . This
# program and a another program communicate through pipes (both input and output)
# according to this architecture . When a command is sent it is indicated
# with a right arrow indicating something is written to the other program’s
# standard input . When the other program sends something to this Python Program
# it is indicated with a left arrow. That means it is written to the standard
# output of the other program.

# Python Other
# 0−−−−−−−−−−−> # NewGame is initiated by the Other Code
# <−−−−−−−−−−−0 # Other Code says OK.
# 2M−−−−−−−−−> # HumanMove followed by Move Value Mwhich is 0−6.
# # Move Value Mwill be on separate line .
# <−−−−−−−−−−−0 # Other Code says OK.
# 1−−−−−−−−−−−> # Computer Move is indicated to Other Code
# <−−−−−−−−−0M # Status OK and Move Value Mwhich is 0−6.
# 3−−−−−−−−−−−> # Game Over?
# <−−−−−−−−−Val # Val is 0=Not Over , 1=Computer Won, 2=HumanWon, 3=Tie .

# This architecture must be adhered to strictly for this program to work. Here
# is sample Lisp code that will handle this interaction . However , the other
# programmay be written in any programming language , including Python.

#(defun play ()
#( let ((gameBoard (make−hash−table : size 10))
#(memo (make−hash−table : size 27 : test #’equalp))
#( lastMove nil ))

#(do () (nil nil )
#;(printBoard gameBoard)
#( let ((msgId (read)))
#(cond ((equal msgId 2) ; ; Human turn to call human turn function
#( setf lastMove (humanTurn gameBoard)))

#((equal msgId 0) ; ; NewGame message
#(progn
#( setf gameBoard (make−hash−table : size 10))
#( setf memo (make−hash−table : size 27 : test #’equalp))
#(format t "0~%")))
#; ; Return a 0 to indicate the computer is ready

#((equal msgId 1) ; ; Computer Turn message
#( setf lastMove (computerTurn gameBoard)))

#((equal msgId 3) ; ; Get Game Status

#(cond ((equal (evalBoard gameBoard lastMove) 1) (format t "1~%"))
#; ; The Computer Won

#((equal (evalBoard gameBoard lastMove) −1) (format t "2~%"))
#; ; The HumanWon

#(( fullBoard gameBoard) (format t "3~%")
#; ; It ’s a draw

#( t (format t "0~%"))))
#; ; The game is not over yet .

#( t (format t "−1~%")))))))

Computer = 1
Human =−1

class Tile(turtle.RawTurtle):
    def __init__(self, canvas, row, col, app):
        super().__init__(canvas)
        self.val = 0
        self.row = row
        self.col = col
        self.tttApplication = app
        self.penup()
        self.ht()
        self.goto(col * 100 + 50, row * 100 + 50)

    def setShape(self, horc, screen):
        self.val = horc
        if horc == Computer:
            self.shape("blackchecker.gif")
        else:
            self.shape("redchecker.gif")
        self.drop(screen)

    def getOwner(self):
        return self.val

    def clicked(self):
        print(self.row, self.col)

    def drop(self, screen):
        self.goto(self.col * 100 + 50, 0)
        screen.tracer(1)
        self.speed(5)
        self.st()
        self.goto(self.col * 100 + 50, self.row * 100 + 55)
        self.goto(self.col * 100 + 50, self.row * 100 + 45)
        self.goto(self.col * 100 + 50, self.row * 100 + 50)
        screen.tracer(0)

class Connect4Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.running = False

    def buildWindow(self):
        self.master.title("Connect Four")
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)
        fileMenu.add_command(label="Exit", command=self.master.quit)
        bar.add_cascade(label="File", menu=fileMenu)
        self.master.config(menu=bar)
        
        canvas = tkinter.Canvas(self, width=700, height=600)
        canvas.pack(side=tkinter.LEFT)
        
        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.ht()
        screen = theTurtle.getscreen()
        screen.setworldcoordinates(0, 600, 700, 0)
        screen.register_shape("blackchecker.gif")
        screen.register_shape("redchecker.gif")
        screen.tracer(0)
        screen.bgcolor("yellow")
        
        theTurtle.width(5)
        for k in range(6):
            theTurtle.penup()
            theTurtle.goto(k * 100 + 100, 0)
            theTurtle.pendown()
            theTurtle.goto(k * 100 + 100, 600)
        
        theTurtle.ht()
        screen.update()

    def checkStatus(self):
        toOther.write("3\n")
        toOther.flush()
        status = int(fromOther.readline().strip())
        if status == 1:
            tkinter.messagebox.showinfo("Game Over", "I Won! ! ! ! !")
        elif status == 2:
            tkinter.messagebox.showinfo("Game Over", "You Won! ! ! ! !")
        elif status == 3:
            tkinter.messagebox.showinfo("Game Over", "It’s a tie.")
        return status

    def ComputerTurn(self):
        toOther.write("1\n")
        toOther.flush()
        status = int(fromOther.readline().strip())
        if status == 0:
            move = int(fromOther.readline())
            row = move // 7
            col = move % 7
            matrix[row][col].setShape(Computer, screen)
            screen.update()

    def HumanTurn(self, x, y):
        if self.running:
            return
        self.running = True
        col = int(x) // 100
        row = 5
        while row >= 0 and matrix[row][col].isvisible():
            row -= 1
        if row < 0:
            self.running = True
            return
        val = row * 7 + col
        toOther.write("2\n")
        toOther.flush()
        toOther.write(str(val) + "\n")
        toOther.flush()
        status = fromOther.readline().strip()
        matrix[row][col].setShape(Human, screen)
        screen.update()
        status = self.checkStatus()
        if status == 0:
            self.ComputerTurn()
            self.checkStatus()
        self.running = False

matrix = []
for i in range(6):
    row = []
    for j in range(7):
        t = Tile(canvas, i, j, self)
        row.append(t)
    matrix.append(row)
screen.update()
screen.onclick(HumanTurn)
sideBar = tkinter.Frame(self, padx=5, pady=5, relief=tkinter.RAISED, borderwidth="5pt")
sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

def NewGame():
    toOther.write("0\n")
    toOther.flush()
    status = int(fromOther.readline().strip())
    for row in matrix:
        for token in row:
            token.ht()
    screen.update()

kb = tkinter.Button(sideBar, text="Pass", command=self.ComputerTurn)
kb.pack()
ng = tkinter.Button(sideBar, text="New Game", command=NewGame)
ng.pack()

proc = subprocess.Popen(["clisp", "c4.fas"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
fromOther = proc.stdout
toOther = proc.stdin

def main():
    root = tkinter.Tk()
    animApp = Connect4Application(root)
    animApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()
