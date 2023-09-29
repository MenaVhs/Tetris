from enum import Enum

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

def tetris():

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


    print_screen(screen)

    screen = move_piece(screen, Movement.ROTATE)



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
                        break
                    
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