from game import InLine

def main():
    game = InLine()
    print_tablero(game)
    while True:
        play = choose_col(game)
        if play == False:
            break
        if game.check_winner() == True:
            print(f'{game.winner} gana')
            play_again = input('Jugar de nuevo(S/N)')
            if play_again == 's' or play_again == 'S':
                game = InLine()
                print_tablero(game)
                continue
            else:
                break
        
def print_tablero(game):
        print('  0    1    2    3    4    5    6')
        for r in game.board:
            print (r)

def choose_col(game):
    try:
        col_input = (input(f'Jugador {game.player} ingrese un número del 0 al 6: '))
        if col_input == 'S' or col_input == 's':
            return False
        col_input = int(col_input)
        try:
            game.throw_coin(col_input)
            print_tablero(game)
        except TypeError:
                print('Columna completa, ingrese otro número')
    except ValueError:
        print('Error, ingrese un número del 0 al 6')
    except IndexError:
        print('Error, ingrese un número del 0 al 6')    


if __name__ == '__main__':
    main()