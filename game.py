__author__ = "tofugangsw@gmail.com"

from board import Board
from itertools import chain
from os import system, name

################################################################################

class Game(object):

################################################################################

    def __init__(self):
        """

        """

        self._board = Board()

################################################################################

    def start(self):
        """

        :return:
        """

        print(">READY")
        print(">PLAYER ONE")
        print(">YOU HAVE " + Board.CIRCLE)

        while not self._is_game_finished():
            self._clear_console()
            self._view()
            self._prompt_player()
            if self._is_game_finished():
                break
            else:
                print(">COMPUTER THINKING...")
                computer_move = self._board.make_computer_move()
                print(">COMPUTER MOVE " + str(computer_move[0]) + str(computer_move[1]))

        self._clear_console()
        if self._have_player_won(self._board.CIRCLE):
            print(">YOU WON!")
        else:
            print(">YOU LOST!")
        self._view()

################################################################################

    def _view(self):
        """

        :return:
        """

        # numbers line
        print("  1 2 3")
        # first line
        print("a " + " ".join(self._board.board[0]))
        # second line
        print("b " + " ".join(self._board.board[1]))
        # third line
        print("c " + " ".join(self._board.board[2]))

################################################################################

    def _clear_console(self):
        """

        :return:
        """

        # Windows
        if name == 'nt':
            _ = system('cls')

        # Mac and Linux (os.name is 'posix')
        else:
            _ = system('clear')

################################################################################

    def _prompt_player(self):
        """

        :return:
        """

        print(">YOUR MOVE?")
        move = input(">")
        while not self._board.is_move_valid(move):
            print(">NOT A VALID MOVE; YOUR MOVE?")
            move = input(">")
        self._board.make_player_move(move)

################################################################################

    def _is_game_finished(self):
        """

        :return:
        """

        return not self._board.EMPTY in list(chain.from_iterable(self._board.board)) \
               or self._have_player_won(self._board.CIRCLE) \
               or self._have_player_won(self._board.CROSS)

################################################################################

    def _have_player_won(self, player: str) -> bool:
        """

        :param player:
        :return:
        """

        # I know, it's a nightmare. The first two parts check if any of the
        # players took any row or column. The last two parts check if any of the
        # players took any diagonal.
        return \
            any([all([
                square == player
                for square in self._board.board[i]])
                for i in range(len(self._board.board))]) \
            or any([all([
                square == player
                for square in [line[i] for line in self._board.board]])
                for i in range(len(self._board.board[0]))]) \
            or all([self._board.board[i][i] == player
                   for i in range(len(self._board.board))]) \
            or all([self._board.board[i][-i - 1] == player
                   for i in range(len(self._board.board))])

################################################################################