class Ship:
    locations = []

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hit_points = size

    def is_sunk(self):
        if self.hit_points <= 0:
            return True
        return False

    def hit(self):
        self.hit_points -= 1
