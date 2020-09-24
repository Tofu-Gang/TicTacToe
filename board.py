__author__ = "tofugangsw@gmail.com"

from typing import List
from random import randrange

################################################################################

class Board(object):
    # these UTF-8 signs work weird in console
    # CROSS = u"\u274C"
    # CIRCLE = u"\u25CB"
    # EMPTY = u"\u26AB"

    CROSS = "X"
    CIRCLE = "O"
    EMPTY = "."

################################################################################

    def __init__(self):
        """

        """

        self._board = [[self.EMPTY, self.EMPTY, self.EMPTY],
                       [self.EMPTY, self.EMPTY, self.EMPTY],
                       [self.EMPTY, self.EMPTY, self.EMPTY]]
        self._player = self.CIRCLE

################################################################################

    @property
    def board(self) -> List[List[str]]:
        """

        :return:
        """

        return self._board

################################################################################

    @property
    def player(self):
        """

        :return:
        """

        return self._player

################################################################################

    def make_player_move(self, move: str) -> None:
        """

        :param player:
        :param move:
        :return:
        """

        # ASCII
        row = ord(move[0]) - ord("a")
        column = int(move[1]) - 1
        self._board[row][column] = self._player
        self._player = self.CROSS

################################################################################

    def is_move_valid(self, move: str) -> bool:
        """

        :param move:
        :param player:
        :return:
        """

        try:
            row = ord(move[0]) - ord("a")
            column = int(move[1]) - 1
        except ValueError:
            return False

        return \
            row in [i for i in range(len(self._board))] \
            and column in [i for i in range(len(self._board[0]))] \
            and self._board[row][column] == self.EMPTY

################################################################################

    def make_computer_move(self):
        """

        :return:
        """

        while True:
            row = randrange(0, 3)
            column = randrange(0, 3)
            if self._board[row][column] == self.EMPTY:
                self._board[row][column] = self.CROSS
                break

        self._player = self.CIRCLE
        return tuple([chr(row + ord("a")), column + 1])

################################################################################