import pyglet as pg
from board import Board



def draw_board(board: Board):

    light_color = (200, 220, 230)
    dark_color = (50, 80, 145)

    batch = pg.graphics.Batch()
    squares = []

    square_size : int = 75


    for i in range(8):
        for j in range(8):
            is_light = (i + j) % 2 != 0

            
            color = light_color if is_light else dark_color
            square = pg.shapes.Rectangle(i * square_size, j * square_size, square_size, square_size, color=color, batch=batch)
            squares.append(square)

    batch.draw()


window = pg.window.Window(caption="Yarmush Engine", width=600, height=600)
board = Board.load_starting_position()

@window.event
def on_draw():
    draw_board(board)


pg.app.run()



