import enum
from collections import namedtuple

# Use emum to represent stone colors
class Player(enum.Enum):
    black = 1
    white = 2

    # class property to switch color
    @property
    def other(self):
        return Player.black if self == Player.white else Player.white

# named tuple to access points as "row" and "col"
class Point(namedtuple ('Point', 'row col')):
    # return neighbors
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1)
        ]