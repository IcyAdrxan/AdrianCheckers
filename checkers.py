
from typing import List
from exceptions import InvalidMoveException
from enum import Enum

"""
    TODO List for Adrian
    1. Finish the __init__ function
        - As a caveat, figure out what each of the variables mean (i.e what does a 1 mean on the board, what does a 2 mean, ...etc.)
    2. Finish the reset_board function
        - This should come quite easily as a result of the __init__ function
    3. Finish is_game_over function
    4. Finish _is_legal_move function
        - Hint! Identify what type of piece is starting out (King, regular piece, empty square, ...etc.)
    5. Finish the make_move function

    NEXT: Start on graphical implementation!

"""

"""
    -1 - Blocked Square
    0 - Free Square
    1 - Red Pawn
    2 - Black Pawn
    3 - Red King
    4 - Black King
"""
class Piece(Enum):
    BLOCKED_SQUARE = -1
    FREE_SQUARE = 0
    RED_PAWN = 1
    BLACK_PAWN = 2
    RED_KING = 3
    BLACK_KING=4
class Turn(Enum):
    RED_TURN = False
    BLACK_TURN = True
class Result(Enum):
    BLACK = 2
    RED = 1
    ONGOING = 0
class CheckersLogic:

    def __init__(self) -> None:
        self.board: List[List[Piece]] = [[Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN],
                                         [Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE],
                                         [Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN],
                                         [Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE],
                                         [Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE],
                                         [Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE],
                                         [Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN],
                                         [Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE]] # TODO Adrian
        self.turn: Turn = Turn.RED_TURN # TODO Adrian
        
    
    
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
        """        
        1. Can only jump to adjacent diagonal squares
        2. Pawns can only move forward
        3. Kings can move backward and forward
        4. Have to jump to a free square
        5. If there is an opponent pawn occupying one of the squares you can jump to AND the square diagonally after the opponent's pawn is a free_square, then turn the opponent's pawn into a free square
        6. If a pawn reaches their opposite last row, then switch PAWN to KING
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
        self.board: List[List[Piece]] = [[Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN],
                                         [Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE],
                                         [Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN, Piece.BLOCKED_SQUARE, Piece.BLACK_PAWN],
                                         [Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE],
                                         [Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE, Piece.BLOCKED_SQUARE, Piece.FREE_SQUARE],
                                         [Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE],
                                         [Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN],
                                         [Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE, Piece.RED_PAWN, Piece.BLOCKED_SQUARE]] # TODO Adrian
        self.turn: Turn = Turn.RED_TURN # TODO Adrian
        # TODO Adrian
        pass
    
    def is_game_over(self) -> int:
        """
        Checks if the game is over and returns the result.
            
        Returns:
            int: Result of the game. 
                0: Game is still ongoing.
                1: Player 1 (red) wins.
                2: Player 2 (black) wins.
            


        """

        red_pawn_exists = False
        red_king_exists = False
        
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if Piece.RED_PAWN == self.board[row][col]:
                    red_pawn_exists = True
                elif Piece.RED_KING== self.board[row][col]:
                    red_king_exists = True
        
        if red_pawn_exists == False and red_king_exists == False:
            return Result.BLACK
        
        black_pawn_exists = False
        black_king_exists = False
        
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if Piece.BLACK_PAWN == self.board[row][col]:
                    black_pawn_exists = True
                elif Piece.BLACK_KING== self.board[row][col]:
                    black_king_exists = True
                
        
        if black_pawn_exists == False and black_king_exists == False:
            return Result.RED
        
        return Result.ONGOING
