class Board:
    def __init__(self, size=(100,100)):
        self.width = size[0]
        self.height = size[1]
        self.boardGen()

    def boardGen(self, function=lambda x,y:0):
        self.board = [
            [function(x,y) for x in range(self.width)] for y in range(self.height)
            ]

    def boardConfig(self,
        pos0 = [],
        pos1 = [(1,1), (2,1)]
        ):
        for y in range(self.height):
            for x in range(self.width):
                if (x,y) in pos0:
                    self.board[y][x] = 0
                if (x,y) in pos1:
                    self.board[y][x] = 1

    def boardNeighbours(self, x, y):
        neighbours = 0
        if y != 0 and x != 0: neighbours += self.board[y-1][x-1]
        if y != 0: neighbours += self.board[y-1][x]
        if y != 0 and x != self.width-1: neighbours += self.board[y-1][x+1]

        if x != 0: neighbours += self.board[y][x-1]
        if x != self.width-1: neighbours += self.board[y][x+1]

        if y != self.height-1 and x != 0: neighbours += self.board[y+1][x-1]
        if y != self.height-1: neighbours += self.board[y+1][x]
        if y != self.height-1 and x != self.width-1: neighbours += self.board[y+1][x+1]

        return neighbours

    def boardTick(self):
        newBoard = [
            [0 for _ in range(self.width)] for __ in range(self.height)
            ]
        for y in range(self.height):
            for x in range(self.width):
                neighbours = self.boardNeighbours(x,y)
                if neighbours < 2: newBoard[y][x] = 0
                elif neighbours == 2: newBoard[y][x] = self.board[y][x]
                elif neighbours == 3: newBoard[y][x] = 1
                else: newBoard[y][x] = 0
        self.board = newBoard

    def __str__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += f"{' ' if self.board[y][x] == 0 else '@'}"
            s += "\n"
        return s
