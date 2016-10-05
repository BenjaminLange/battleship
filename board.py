import os


class Board():
    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
    COLUMNS = 'abcdefghijklmnopqrstuvwxyz'

    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)
    ]

    def __init__(self):
        self.board_size = 10
        # self.board = [(x, y) for x in self.HEADER[:self.BOARD_SIZE]
        # for y in range(self.BOARD_SIZE)]
        self.board = [[Board.EMPTY for x in range(self.board_size)]
                      for y in range(self.board_size)]

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + self.board_size)]))

    def print_board(self):
        self.print_board_heading()
        # print(self.board)

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
        for ship in Board.SHIP_INFO:
            self.get_location(ship)
            self.clear_screen()
            self.print_board()
        input("When you are finished reviewing your board, "
              "Press enter to continue...")
        self.clear_screen()

    def get_location(self, ship):
        ship_name = ship[0]
        ship_size = ship[1]
        location = input("Place the location of the {} ({} spaces): "
                         .format(ship_name, ship_size)).strip().lower()
        

        try:
            column, row = location[0], int(location[1:]) - 1
        except ValueError:
            print("The row must be a number.")
            return self.get_location(ship)
        if column not in 'abcdefghij':
            print("{} is not a valid column.".format(column))
            return self.get_location(ship)
        elif not 0 <= row < self.board_size + 1:
            print("{} is not a valid row.".format(row))
            return self.get_location(ship)
        else:
            horizontal = input("Is it horizontal? (Y)/N: ").strip().lower()
            if horizontal == 'n':
                horizontal = False
            else:
                horizontal = True
            column = Board.COLUMNS.index(column)
            self.check_placement(column, row, horizontal, ship)

    def check_placement(self, column, row, horizontal, ship):
        ship_name = ship[0]
        ship_size = ship[1]
        if horizontal:
            if column + ship_size > self.board_size:
                self.clear_screen()
                print("The {} will not fit there. Try again."
                      .format(ship_name))
                self.print_board()
                return self.get_location(ship)
            for col in range(column, column + ship_size):
                if self.board[row][col] == Board.EMPTY:
                    continue
                else:
                    self.clear_screen()
                    print("The {} will not fit there. Try again."
                          .format(ship_name))
                    self.print_board()
                    return self.get_location(ship)
            for col in range(column, column + ship_size):
                    self.board[row][col] = Board.HORIZONTAL_SHIP
        else:
            if row + ship_size > self.board_size:
                self.clear_screen()
                print("The {} will not fit there. Try again."
                      .format(ship_name))
                self.print_board()
                return self.get_location(ship)
            for rw in range(row, row + ship_size):
                if self.board[rw][column] == Board.EMPTY:
                    continue
                else:
                    print("The {} will not fit there. Try again."
                          .format(ship_name))
                    return self.get_location(ship)
            for rw in range(row, row + ship_size):
                self.board[rw][column] = Board.VERTICAL_SHIP

    def is_valid_location(self, location):
        try:
            column, row = location[0], int(location[1:]) - 1
        except ValueError:
            print("The row must be a number.")
            return False
        if column not in 'abcdefghij':
            print("{} is not a valid column.".format(column))
            return False
        elif not 0 <= row < self.board_size + 1:
            print("{} is not a valid row.".format(row))
            return False
        else:
            return True

    def check_for_hit(self, location):
        pass

    def check_for_loss(self):
        if self.board.count(Board.HIT) == 17:
            return True
        return False
