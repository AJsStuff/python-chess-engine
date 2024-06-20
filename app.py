import pyglet as pg
from piece import Piece
from board import Board



def draw_board(board: Board):

    light_color = (200, 220, 230)
    dark_color = (50, 80, 145)

    batch = pg.graphics.Batch()
    board_layer = pg.graphics.Group(0)
    piece_layer = pg.graphics.Group(1)
    
    squares = []

    square_size : int = 75

    pieces_dict = {
        Piece.King : "king",
        Piece.Queen : "queen",
        Piece.Bishop : "bishop",
        Piece.Knight : "knight",
        Piece.Rook : "rook",
        Piece.Pawn : "pawn",
    }


    for i in range(8):
        for j in range(8):
            is_light = (i + j) % 2 != 0

            
            color = light_color if is_light else dark_color
            square = pg.shapes.Rectangle(i * square_size, j * square_size, square_size, square_size, color=color, batch=batch, group=board_layer)
            squares.append(square)

            cp = board.rep[i*8 + j]
            if cp != 0:
                print(cp & Piece.White)
                print(cp)

                if (cp & Piece.White):
                    img = pg.image.load("assets/king_white.png")
                else:
                    img = pg.image.load("assets/king_black.png")

                sprite = pg.sprite.Sprite(img=img, batch=batch, group=piece_layer)
                sprite.x = j * square_size
                sprite.y = i * square_size
                squares.append(sprite)

    batch.draw()


window = pg.window.Window(caption="Yarmush Engine", width=600, height=600)
board = Board.load_position_from_FEN("8/5k2/3p4/1p1Pp2p/pP2Pp1P/P4P1K/8/8 b - - 99 50")

@window.event
def on_draw():
    draw_board(board)


pg.app.run()



