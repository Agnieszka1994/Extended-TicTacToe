
from board import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--size')
args = parser.parse_args()


ticTacToe = Board(int(args.size))
ticTacToe.print_matrix()
print('X starts!')
while True:
    # check if we have a winner
    if not ticTacToe.has_anyone_won():
        # check if we can play
        if ticTacToe.game_possible():
            credentials = input()
            char_assigned = False
            if ticTacToe.credentials_correct(credentials):
                char_assigned = ticTacToe.try_assign(int(credentials[0]), int(credentials[2]))
                if char_assigned:
                    ticTacToe.switch_tour()
                    ticTacToe.print_matrix()
        else:
            break
    else:
        break
