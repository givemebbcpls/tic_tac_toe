from gameparts import Board
from gameparts import FieldIndexError, CellOccupiedError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    while running:
        print(f'Turn of player {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except CellOccupiedError:
                print('Cell is busy, enter another coords.')
            except FieldIndexError:
                print(
                    'Your value out of field bound, should be positive and '
                    f'less than {game.field_size}'
                )
                print('Enter numbers again...')
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                    )
            except Exception as e:
                print(f'Raise error: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        if (game.check_win(current_player)):
            game.save_result(f'{current_player} win')
            print(f'\'{current_player}\' you are win!')
            running = False
        elif (game.is_board_full()):
            game.save_result('draw')
            print('It\'s a draw!')
            running = False
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
