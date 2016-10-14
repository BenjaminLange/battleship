import os

from ship import Ship


class Board():
    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
    COLUMNS = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        self.board_size = 10
        self.board = [[Board.EMPTY for x in range(self.board_size)]
                      for y in range(self.board_size)]
        self.ship_info = [
            Ship("Aircraft Carrier", 5),
            Ship("Battleship", 4),
            Ship("Submarine", 3),
            Ship("Cruiser", 3),
            Ship("Patrol Boat", 2)
        ]

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in
                                range(ord('A'), ord('A') + self.board_size)]))

    def print_board(self):
        self.print_board_heading()

        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def place_ships(self):
        for ship in self.ship_info:
            self.get_location(ship)
            self.clear_screen()
            self.print_board()
        input("When you are finished reviewing your board, "
              "Press enter to continue...")
        self.clear_screen()

    def get_location(self, ship):
        location = input("Place the location of the {} ({} spaces): "
                         .format(ship.name, ship.size)).strip().lower()
        if self.is_valid_location(location):
            horizontal = input("Is it horizontal? (Y)/N: ").strip().lower()
            if horizontal == 'n':
                horizontal = False
            else:
                horizontal = True
            self.check_placement(location, horizontal, ship)
        else:
            return self.get_location(ship)

    def check_placement(self, location, horizontal, ship):
        column, row = Board.COLUMNS.index(location[0]), int(location[1:]) - 1
        if horizontal:
            if column + ship.size > self.board_size:
                self.clear_screen()
                print("The {} will not fit there. Try again."
                      .format(ship.name))
                self.print_board()
                return self.get_location(ship)
            for col in range(column, column + ship.size):
                if self.board[row][col] == Board.EMPTY:
                    continue
                else:
                    self.clear_screen()
                    print("The {} will not fit there. Try again."
                          .format(ship.name))
                    self.print_board()
                    return self.get_location(ship)
            locations = []
            for col in range(column, column + ship.size):
                locations.append((row, col))
                self.board[row][col] = Board.HORIZONTAL_SHIP
            ship.locations = locations
        else:
            if row + ship.size > self.board_size:
                self.clear_screen()
                print("The {} will not fit there. Try again."
                      .format(ship.name))
                self.print_board()
                return self.get_location(ship)
            for rw in range(row, row + ship.size):
                if self.board[rw][column] == Board.EMPTY:
                    continue
                else:
                    self.clear_screen()
                    print("The {} will not fit there. Try again."
                          .format(ship.name))
                    self.print_board()
                    return self.get_location(ship)
            locations = []
            for rw in range(row, row + ship.size):
                locations.append((rw, column))
                self.board[rw][column] = Board.VERTICAL_SHIP
            ship.locations = locations

    def is_valid_location(self, location):
        try:
            column, row = location[0].lower(), int(location[1:])
        except ValueError:
            print("The row must be a number.")
            return False
        except IndexError:
            print("Make sure you enter a column and a row!")
            return False
        if column not in 'abcdefghij':
            print("{} is not a valid column.".format(column))
            return False
        elif not 0 <= row < self.board_size + 1:
            print("{} is not a valid row.".format(row))
            return False
        else:
            return True

    def is_already_guessed(self, location):
        column, row = Board.COLUMNS.index(location[0].lower()), int(location[1:]) - 1
        location = self.board[row][column]
        if(location == Board.HIT or
           location == Board.MISS or
           location == Board.SUNK):
            print("You've already guessed that location!")
            return True
        return False

    def check_for_hit(self, location):
        column, row = Board.COLUMNS.index(location[0].lower()), int(location[1:]) - 1
        target = self.board[row][column]
        location = row, column
        if(target == Board.VERTICAL_SHIP or
           target == Board.HORIZONTAL_SHIP):
            print("HIT!!")
            for ship in self.ship_info:
                if location in ship.locations:
                    ship.hit()
            return True
        else:
            print("Miss!")
            return False

    def set_location_hit(self, location):
        column, row = Board.COLUMNS.index(location[0].lower()), int(location[1:]) - 1
        self.board[row][column] = Board.HIT

    def set_location_miss(self, location):
        column, row = Board.COLUMNS.index(location[0].lower()), int(location[1:]) - 1
        self.board[row][column] = Board.MISS

    def check_for_sunk_ship(self, player):
        for ship in self.ship_info:
            if ship.is_sunk():
                print("{}, you sunk the {}!".format(player.name, ship.name))
                for location in ship.locations:
                    row, column = location
                    self.board[row][column] = self.SUNK
                    player.hit_miss_board.board[row][column] = self.SUNK
                self.ship_info.remove(ship)

    def set_ship_sunk(self, ship):
        for location in ship.locations:
            column, row = location
            column = Board.COLUMNS.index(column)
            row -= 1
            self.board[row][column] = self.SUNK

    def check_for_loss(self):
        if sum(row.count(self.SUNK) for row in self.board) == 17:
            return True
        return False
