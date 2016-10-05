import os

from player import Player


class Game():
    player_one = None
    player_two = None

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def __init__(self):
        self.setup()
        self.play()

    def setup(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')
        self.clear_screen()
        print("{}, place your ships on the board."
              .format(self.player_one.name))
        self.player_one.board.print_board()
        self.player_one.board.place_ships()
        print("{}, place your ships on the board."
              .format(self.player_two.name))
        self.player_two.board.print_board()
        self.player_two.board.place_ships()
        input("{}, press enter to start the game..."
              .format(self.player_one.name))

    def play(self):
        while(not self.player_one.board.check_for_loss() and
              not self.player_two.board.check_for_loss()):
            print("{}, here is your board.".format(self.player_one.name))
            self.player_one.board.print_board()
            input("{}, press enter to continue..."
                  .format(self.player_one.name))
            self.clear_screen()
            self.player_one.hit_miss_board.print_board()
            location = input("{}, select a target: ".format(self.player_one.name))
            while not self.player_one.hit_miss_board.is_valid_location(location):
                location = input("{}, select a target: ".format(self.player_one.name))

            # select target location
            # validate location is on board and hasn't already been guessed
                # location should be Board.EMPTY, Board.VERTICAL_SHIP,
                # or Board.HORIZONTAL_SHIP. Otherwise, allow for another guess
                # update other player's board with a hit or a miss
                # update current palyer's hit/miss board with a hit or a miss
                # check for win
                # display updated hit/miss board
                # clear screen and display message prompting next player's turn
                # go to next player's turn


Game()
