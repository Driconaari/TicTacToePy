# Tic-Tac-Toe AI

This is a simple Tic-Tac-Toe game implemented in Python with an AI opponent. The AI uses the Minimax algorithm with alpha-beta pruning to determine the best moves. The difficulty of the AI can be adjusted by setting the search depth.

## Features

- Play as either X or O
- Adjustable difficulty level (search depth)
- AI opponent using Minimax algorithm with alpha-beta pruning
- Clear indication of the winner or a draw

## How to Play

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/<username>/TicTacToePy.git
    cd TicTacToePy
    ```

2. Run the game:
    ```sh
    python TicTacToeAi.py
    ```

3. Follow the prompts to choose your player (X or O) and set the difficulty level (search depth between 1 and 10).

4. Enter your moves by specifying the row and column numbers (1-3).

5. The game will display the board after each move and indicate the winner or if it's a draw.

## Example
Choose your player (X/O): X Enter the difficulty level (search depth) between 1 and 10: 3 . . . . . . . . .

Enter row and column (1-3): 1 1 X . . . . . . . .

AI is making a move... X . . . O . . . .

Enter row and column (1-3): 1 2 X X . . O . . . .

AI is making a move... X X . . O O . . .

Enter row and column (1-3): 1 3 X X X . O O . . .

X wins


## Requirements

- Python 3.x

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

