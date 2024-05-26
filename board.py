from piece import *
import math

class Board:

    def __init__(self):
        self.rep = [[0 for file in range(8)] for rank in range(8)]

        self.white_castle_kingside: bool = True
        self.white_castle_queenside: bool = True
        self.black_castle_kingside: bool = True
        self.black_castle_queenside: bool = True
    

    def __str__(self) -> str:
        output = ""
        for rank in self.rep:
            output += f"{str(rank)}\n" 
        
        return output

    def place_piece(self, position: int, piece: Piece):
        rank = math.floor(position / 8)
        file = position % 8

        self.rep[rank][file] = piece.id
    
    @classmethod
    def load_position_from_FEN(cls, fen: str):
        board = cls()
        fen = fen.strip()

        piece_dictionary = {
            "k" : King("black"),
            "K" : King("white"),
            "q" : Queen("black"),
            "Q" : Queen("white"),
            "r" : Rook("black"),
            "R" : Rook("white"),
            "b" : Bishop("black"),
            "B" : Bishop("white"),
            "n" : Knight("black"),
            "N" : Knight("white"),
            "p" : Pawn("black"),
            "P" : Pawn("white"),
            
        }

        rank, file = 0, 0

        for char in fen:
            if char == "/":
                rank += 1
                file = 0
            else:
                print(char)
                if char.isdigit():
                    print(f"added: {int(char)}")
                    file += int(char)
                else:
                    print(rank * 8 + file)
                    print(f"rank: {rank}, file:{file}")
                    board.place_piece(rank * 8 + file, piece_dictionary[char])
                    file += 1


        return board


board = Board.load_position_from_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
print(board)
        