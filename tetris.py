from enum import Enum

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

class Figure():
    def __init__(self):
        self.T = [["🔳","🔳", "🔳"],
                  ["🔲","🔳", "🔲"], 
                  ["🔲","🔳", "🔲"]]
        
        self.I = [["🔳","🔳","🔳","🔳","🔳"]]

        self.L = [["🔳", "🔲"], 
                  ["🔳", "🔲"], 
                  ["🔳", "🔲"], 
                  ["🔳", "🔳"]]

    def rotate_piece(self, piece):
        rows = len(piece)
        columns = len(piece[0])

        # matriz vacía para almacenar la pieza rotada
        rotated_piece = [['🔲'] * rows for _ in range(columns)]
        print("rotsación", rotated_piece)

        # rotación de la pieza
        for i in range(rows):
            for j in range(columns):
                rotated_piece[j][rows - 1 - i] = piece[i][j]
        return rotated_piece

def tetris():
    import random

    screen = [["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
              ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"]]
    current_piece = None

    print_screen(screen)

    current_piece = random.choice([Figure().T, Figure().I, Figure().L])
    screen = add_piece_to_board(screen, current_piece)
    
    screen = move_piece(screen, Movement.RIGHT)
    screen = move_piece(screen, Movement.ROTATE)

    current_piece = Figure().rotate_piece(current_piece)



def print_screen(screen: list):

    print(" Pantalla Tetris ".center(30,'*'))
    for row in screen:
        print("".join(map(str, row)))
    
    # Other way
    # for row in screen:
    #     for i, element in enumerate(row):
    #         print(element, end="")
    #         if i == len(row) - 1:
    #             print()

def add_piece_to_board(board: list, figure: list):
    board_rows = len(board)
    board_columns = len(board[0])
    print(board_rows, board_columns)
    figure_rows = len(figure)
    figure_cols = len(figure[0])
    print(figure_rows, figure_cols)

    # posición inicial de la figura en el tablero
    start_col = (board_columns - figure_cols) // 2
    start_row = 0

    # colocar posición inicial de la figura
    board = [[board[start_row + i][start_col + j] for j in range(figure_cols)] for i in range(figure_rows)]

    return board

def move_piece(screen: list,movement: Movement) -> list: # Movement le indica qué acción deberá hacer/ '->' se usa para indicar el return

    # Nueva matriz para crear una pantalla
    new_screen = [['🔲'] * 10 for _ in range(10)]

    count = 1
    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):  # item is then column
            if item == "🔳":
                new_row_index = 0
                new_column_index = 0

                match movement:
                    case Movement.DOWN:
                        new_row_index =  row_index + 1
                        new_column_index = column_index

                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                    case Movement.ROTATE:
                        rotated_piece = Figure().rotate_piece(Figure().L)
                        new_screen[new_row_index][new_column_index] = rotated_piece

                # marcar límites de bordes
                if new_row_index >= len(screen[0]) or new_column_index > len(screen[1]) or new_column_index < 0:
                    print(f"\nLlegó al límite {count}\n") # se va a imprimir el # de veces donde no se podrá a imprimir 
                    # count += 1
                    return screen
                else:
                    # actualizor la pantalla con los movimientos con la ficha negra
                    new_screen[new_row_index][new_column_index] = '🔳'
    print_screen(new_screen)
    return new_screen

tetris()