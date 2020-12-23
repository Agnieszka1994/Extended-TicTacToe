class Board:
    def __init__(self, matrix_size: int):
        self.matrix = [['_' for x in range(matrix_size)] for y in range(matrix_size)]
        self.main_diagonal = self.get_main_diagonal()
        self.secondary_diagonal = self.get_secondary_diagonal()
        self.current_tour = 'X'

    def print_matrix(self):
        if self.matrix:
            print((2 * len(self.matrix[0]) + 3) * '-')
            for row in self.matrix:
                print(f'|', end=" ")
                for element in row:
                    print(f'{element}', end=" ")
                print(f'|')
            print((2 * len(self.matrix[0]) + 3) * '-')

    def get_main_diagonal(self):
        coordinates = []
        row = 0
        col = 0
        for _ in self.matrix:
            coordinates.append([row, col])
            row += 1
            col += 1
        return coordinates

    def get_secondary_diagonal(self):
        coordinates = []
        row = 0
        col = len(self.matrix) - 1
        for _ in self.matrix:
            coordinates.append([row, col])
            row += 1
            col -= 1
        return coordinates

    def has_anyone_won(self) -> bool:
        return self.check_horizontally() or self.check_vertically() \
                or self.check_main_diagonal() or self.check_secondary_diagonal()

    def check_horizontally(self):
        for row in self.matrix:
            potential_winner = row[0]
            if potential_winner != '_':
                for ele in row:
                    if ele != potential_winner:
                        break
                else:
                    print(f'{potential_winner} won!')
                    return True
                return False
            else:
                return False

    def check_vertically(self):
        for i, _ in enumerate(self.matrix):
            potential_winner = self.matrix[0][i]
            if potential_winner != '_':
                for row in self.matrix:
                    if row[i] != potential_winner:
                        break
                else:
                    print(f'{potential_winner} won!')
                    return True
                return False
            else:
                return False

    def check_main_diagonal(self):
        potential_winner = self.matrix[0][0]
        if potential_winner != '_':
            for coords in self.main_diagonal:
                if potential_winner != self.matrix[coords[0]][coords[1]]:
                    break
                potential_winner = self.matrix[coords[0]][coords[1]]
            else:
                print(f'{potential_winner} won!')
                return True
            return False
        else:
            return False

    def check_secondary_diagonal(self):
        potential_winner = self.matrix[0][len(self.matrix) - 1]
        if potential_winner != '_':
            for coords in self.secondary_diagonal:
                if potential_winner != self.matrix[coords[0]][coords[1]]:
                    break
                potential_winner = self.matrix[coords[0]][coords[1]]
            else:
                print(f'{potential_winner} won!')
                return True
            return False
        else:
            return False

    def game_possible(self) -> bool:
        O_count = 0
        X_count = 0
        blanks = 0
        for row in self.matrix:
            for el in row:
                if el == 'O':
                    O_count += 1
                if el == 'X':
                    X_count += 1
                if el == '_':
                    blanks += 1
        if abs(O_count - X_count) > 1:
            print('Impossible')
            return False
        if blanks > 0:
            print('Enter the coordinates:\n')
            return True
        else:
            print('Draw')
            return False

    def credentials_correct(self, credentials) -> bool:
        try:
            row, column = list(map(int, credentials.split()))
            if row > len(self.matrix) or column > len(self.matrix[0])\
                    or row < 1 or column < 1:
                print('Coordinates out of range!')
                return False
            else:
                return True
        except ValueError:
            print('Invalid input! You should enter exactly 2 integers!\n')
            return False

    def try_assign(self, x, y):
        row_idx = x - 1
        col_idx = y - 1
        if self.matrix[row_idx][col_idx] == '_':
            self.matrix[row_idx][col_idx] = self.current_tour
            return True
        else:
            print('This cell is occupied! Choose another one!')
            return False

    def switch_tour(self):
        if self.current_tour == 'X':
            self.current_tour = 'O'
        else:
            self.current_tour = 'X'
