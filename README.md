# Tic Tac Toe
The extended versionof `Tic-tac-toe` is a game for two players, `X` and `O`, who take turns marking the spaces in a `N x N` grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.
The `N` size should be provided as a command-line argument.

In order to place your mark, you need to provide 2 credentials, column and row, following the below pattern:

```
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)
```
## Get started!
- download the repository
```shell
git clone https://github.com/Agnieszka1994/Extended-TicTacToe
cd .\Extended-TicTacToe\
```
- run the program in the command-line
```
Extended-TicTacToe> python main.py <--size=integer_value_greater_than_3>
```
**Sample usage**
```
python main.py --size=13
-----------------------------
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ |
-----------------------------
X starts!
Enter the coordinates:
```
The program executes the below steps:

Prints an empty field at the beginning of the game.
Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a field with the changes if everything is ok.
Ends the game when someone wins or there is a draw.