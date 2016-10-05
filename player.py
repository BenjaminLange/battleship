from board import Board


class Player():
    def __init__(self, player_number):
        self.name = input("What is your name, {}? ".format(player_number))
        self.board = Board()
        self.hit_miss_board = Board()
