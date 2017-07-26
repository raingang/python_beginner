def damaged_or_sunk(board, attacks):
    '''
    https://www.codewars.com/kata/battle-ships-sunk-damaged-or-not-touched/python
    '''
    not_touched = []
    damaged = []
    sunk = []
    points = 0
    unwrapped_board = []
    for y in board:
        for x in y:
            unwrapped_board.append(x)
    for strike in attacks:
        x, y = strike
        hit_point = board[len(board) - y][x - 1]
        if hit_point != 0:
            board[len(board) - y][x - 1] = 0
            unwrapped_board = []
            for y in board:
                for x in y:
                    unwrapped_board.append(x)
            if damaged.count(hit_point) == 0:
                damaged.append(hit_point)
                print(damaged)
            if unwrapped_board.count(hit_point) == 0:
                sunk.append(hit_point)
                damaged = list(filter(lambda x: x != hit_point, damaged))

    for dot in unwrapped_board:
        if dot != 0:
            if not_touched.count(dot) == 0:
                if damaged.count(dot) == 0:
                    not_touched.append(dot)
    points = len(sunk) + 0.5*len(damaged) - len(not_touched)
    return {'sunk': len(sunk), 'damaged': len(damaged), 'not_touched': len(not_touched), 'points': points}


board = [[0, 0, 1, 2, 2, 0], [0, 3, 0, 1, 0, 0],
         [0, 3, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0]]
attacks = [[1, 1], [1, 1], [1, 1]]
print(damaged_or_sunk(board, attacks))
