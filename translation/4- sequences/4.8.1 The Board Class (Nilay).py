class Board:
    # When a board is constructed, you may want to make a copy of the board.
    # This can be a shallow copy of the board because Turtle objects are
    # immutable from the perspective of a board object.
    def __init__(self, board=None):
        self.items = []
        for i in range(3):
            rowlst = []
            for j in range(3):
                if board is None:
                    rowlst.append(Dummy())
                else:
                    rowlst.append(board[i][j])
            self.items.append(rowlst)

    # The getitem method is used to index into the board. It should
    # return a row of the board. That row itself is indexable (it is just
    # a list) so accessing a row and column in the board can be written
    # board[row][column] because of this method.
    def __getitem__(self, index):
        return self.items[index]

    # This method should return true if the two boards, self and other,
    # represent exactly the same state.
    def __eq__(self, other):
        pass

    # This method will mutate this board to contain all dummy
    # turtles. This way the board can be reset when a new game
    # is selected. It should NOT be used except when starting
    # a new game.
    def reset(self):
        screen.tracer(1)
        for i in range(3):
            for j in range(3):
                self.items[i][j].goto(-100, -100)
                self.items[i][j] = Dummy()
        screen.tracer(0)

    # This method should return an integer representing the
    # state of the board. If the computer has won, return 1.
    # If the human has won, return -1. Otherwise, return 0.
    def eval(self):
        pass

    # This method should return True if the board
    # is completely filled up (no dummy turtles).
    # Otherwise, it should return False.
    def full(self):
        pass

    # This method should draw the X’s and O’s
    # of this board on the screen.
    def drawXOs(self):
        for row in range(3):
            for col in range(3):
                if self[row][col].eval() != 0:
                    self[row][col].st()
                    self[row][col].goto(col * 100 + 50, row * 100 + 50)
        screen.update()