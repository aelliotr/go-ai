from dlgo.gotypes import Point

def is_point_an_eye(board, point, color):
    # An empty point is not an eye.
    if board.get(point) is not None:
        return False
    # All adjacent points must contain friendly stones.
    for neighbor in point.neighbors():
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False
    # Count corners occupied by friendly stones and corners off the board.
    friendly_corners = 0
    off_board_corners = 0
    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1)
    ]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(corner)
            if corner_color == corner:
                friendly_corners += 1
        else:
            off_board_corners += 1
    # For eyes with off-board corners, all on-board corners must have friendly stones.     
    if off_board_corners > 0:
        return off_board_corners + friendly_corners == 4
    # For eyes without off-board corners, 3 corners must have friendly stones.
    return friendly_corners >= 3