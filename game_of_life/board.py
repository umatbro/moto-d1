from copy import deepcopy
from game_of_life.cell import Cell, DEAD, ALIVE


class Board:
    def __init__(self, size):
        self.board = []
        for i in range(size):
            self.board.append([Cell(DEAD) for i in range(size)])
            self.prev_board = deepcopy(self.board)

    def update(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                cell_neighbours = self.get_neighbour_states(row, col)
                self[row, col].will_survive(cell_neighbours)

    def get_neighbour_states(self, row, col):
        """
        Get neighbours in order: left, topleft, top, righttop, right, botright, bot, leftbot

        :return:
        """
        neighbour_states = []
        neighbour_states.append(self[row, col-1].state)   # left
        neighbour_states.append(self[row-1, col-1].state) # topleft
        neighbour_states.append(self[row-1, col].state)   # top
        neighbour_states.append(self[row-1, col+1].state) # topright
        neighbour_states.append(self[row, col+1].state)   # right
        neighbour_states.append(self[row+1, col+1].state) # right-bottom
        neighbour_states.append(self[row+1, col].state)   # bottom
        neighbour_states.append(self[row+1, col-1].state) # left-bottom

        return neighbour_states

    def __str__(self):
        result = ''
        for row in self.board:
            for cell in row:
                result += 'x' if cell.state == ALIVE else 'o'
            result += '\n'
        return result

    def __getitem__(self, item):
        row, col = item[0], item[1]
        if row < 0 or row > len(self.prev_board) - 1:
            return Cell(None)
        if col < 0 or row > len(self.prev_board) - 1:
            return Cell(None)
        return self.prev_board[row][col]

    def __setitem__(self, key, value):
        row, cell = key[0], key[1]
        self.board[row][cell] = value


if __name__ == '__main__':
    board = Board(3)
    print(board)
    board[0, 1] = Cell(ALIVE)
    print(board)
    print(board[1, 1].state)