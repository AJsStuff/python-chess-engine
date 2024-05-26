from piece import *
import math



class Board:

    STARTING_POSITION_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    def __init__(self):
        self.rep = [[0 for file in range(8)] for rank in range(8)]

        self.color_to_move = "white"

        self.white_castle_kingside: bool = True
        self.white_castle_queenside: bool = True
        self.black_castle_kingside: bool = True
        self.black_castle_queenside: bool = True

        self.en_passant_square: int = -1

        self.num_of_halfmoves: int = 0
        self.num_of_moves: int = 0
    

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
        fen = fen.strip().split()
        

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

        # Placing Pieces
        for char in fen[0]:
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


        # Color to move
        board.color_to_move == "white" if fen[1] == "w" else "black"


        # Castling rights
        if fen[2] == "-":
            board.white_castle_kingside = False
            board.white_castle_queenside = False
            board.black_castle_kingside = False
            board.black_castle_queenside = False
        else:
            if "K" in fen[2]:
                board.white_castle_kingside = True
            
            if "k" in fen[2]:
                board.black_castle_kingside = True

            if "Q" in fen[2]:
                board.white_castle_queenside = True
            
            if "q" in fen[2]:
                board.black_castle_queenside = True


        # En Passant Squares
        if "-" == fen[3]:
            board.en_passant_square = -1
        else:
            file_dict = {
                "a" : 0,
                "b" : 1,
                "c" : 2,
                "d" : 3,
                "e" : 4,
                "f" : 5,
                "g" : 6,
                "h" : 7,
            }

            rank, file = 8 - int(fen[3][1]), file_dict[fen[3][0]]
            board.en_passant_square = rank * 8 + file
        

        # Halfmoves & Fullmoves
        board.num_of_halfmoves = int(fen[4])
        board.num_of_moves = int(fen[5])
        return board

    @classmethod
    def load_starting_position(cls):
        return cls().load_position_from_FEN(cls().STARTING_POSITION_FEN)


        