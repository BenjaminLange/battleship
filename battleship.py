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
        self.clear_screen()

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

    def play(self):
        while(not self.player_one.board.check_for_loss() and
              not self.player_two.board.check_for_loss()):
            self.play_turn(self.player_one, self.player_two)
            if self.player_two.board.check_for_loss():
                break
            self.play_turn(self.player_two, self.player_one)

    def play_turn(self, player, opponent):
        self.clear_screen()
        input("{}, press enter to start your turn...".format(player.name))
        print("{}, here is your board...".format(player.name))
        player.board.print_board()
        input("{}, press enter to continue..."
              .format(player.name))
        self.clear_screen()
        print("{}, here is {}'s board..."
              .format(player.name, opponent.name))
        player.hit_miss_board.print_board()

        location = input("{}, select a target: "
                         .format(player.name))
        while(not player.hit_miss_board
              .is_valid_location(location) or
              player.hit_miss_board
              .is_already_guessed(location)):
            self.clear_screen()
            print("{}, here is {}'s board..."
                  .format(player.name, opponent.name))
            player.hit_miss_board.print_board()
            location = input("{}, select a target: "
                             .format(player.name))

        self.clear_screen()

        if opponent.board.check_for_hit(location):
            opponent.board.set_location_hit(location)
            player.hit_miss_board.set_location_hit(location)
            opponent.board.check_for_sunk_ship(player)
        else:
            player.hit_miss_board.set_location_miss(location)

        print("{}, here is {}'s board..."
              .format(player.name, opponent.name))
        player.hit_miss_board.print_board()
        if opponent.board.check_for_loss():
            self.game_over(player)
        input("{}, press enter to end your turn...".format(player.name))

    def game_over(self, player):
        print("Congrats {}, you won!!".format(player.name))
        input("Press enter to see the final boards...")
        print("Here are the final boards...")
        self.player_one.print_board()
        self.player_two.print_board()


Game()
