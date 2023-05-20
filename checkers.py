from typing import List
from exceptions import InvalidMoveException

class CheckersLogic:

    def __init__(self) -> None:
        self.board: List[int] = [] # TODO Adrian
        self.turn: bool = 0 # TODO Adrian
        
    def _is_legal_move(self, turn: bool, s_row: int, s_col: int, e_row: int, e_col: int) -> bool:
        """
        Checks if a move is legal based on the given parameters.

        Args:
            turn (bool): Indicates the player's turn. True for player 1, False for player 2.
            s_row (int): The starting row of the piece.
            s_col (int): The starting column of the piece.
            e_row (int): The ending row of the move.
            e_col (int): The ending column of the move.

        Returns:
            bool: True if the move is legal, False otherwise.

        Raises:
            ValueError: If any of the input parameters are out of bounds or invalid.

        """
        # TODO Adrian
        pass
    
    def make_move(self, s_row: int, s_col: int, e_row: int, e_col: int) -> None:
        """
        Makes a move on the game board from the starting position to the ending position.

        Args:
            s_row (int): The starting row of the piece.
            s_col (int): The starting column of the piece.
            e_row (int): The ending row of the move.
            e_col (int): The ending column of the move.

        Returns:
            None

        Raises:
            ValueError: If any of the input parameters are out of bounds or invalid.
            InvalidMoveError: If the move is not allowed according to the game's rules.


        """
        # TODO Adrian
        pass

    def reset_board(self):
        """
        Resets the game board to its initial state.

        Args:
            None

        Returns:
            None

        """

        # TODO Adrian
        pass

    def is_game_over(self) -> int:
        """
        Checks if the game is over and returns the result.

        Returns:
            int: Result of the game. 
                0: Game is still ongoing.
                1: Player 1 (white) wins.
                2: Player 2 (black) wins.
                3: Game ends in a draw.

        """
        # TODO Adrian
        pass