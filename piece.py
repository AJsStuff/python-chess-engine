


class Piece:

    def __init__(self, color: str = "white"):
        self.color = color.lower()
        self.id = 0 if self.color == "white" else 10

    def __int__(self):
        return self.id



class King(Piece):

    value = 200000

    def __init__(self, color: str = "white"):
        super.__init__(color)
        self.id += 6


class Queen(Piece):

    value = 900

    def __init__(self, color: str = "white"):
        super.__init__(color)
        self.id += 5


class Rook(Piece):

    value = 500

    def __init__(self, color: str = "white"):
        super.__init__(color)
        self.id += 4
    

class Bishop(Piece):

    value = 350

    def __init__(self, color: str = "white"):
        super.__init__(color)
        self.id += 3


class Knight(Piece):

    value = 300

    def __init__(self, color: str = "white"):
        super.__init__(color)
        self.id += 2


class Pawn(Piece):

    value = 100

    def __init__(self, color: str = "white"):
        super.__init__(color)
        self.id += 1