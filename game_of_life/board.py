import traceback
from copy import deepcopy
from game_of_life.cell import Cell, DEAD, ALIVE


class Board:
    def __init__(self, size):
        self.board = []
        for i in range(size):
            self.board.append([Cell(DEAD) for j in range(size)])
        self.prev_board = deepcopy(self.board)

    def update(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                cell_neighbours = self.get_neighbour_states(row, col)
                if self[row, col].will_survive(cell_neighbours):
                    self[row, col] = Cell(ALIVE)
                else:
                    self[row, col] = Cell(DEAD)

        self.prev_board = deepcopy(self.board)
        return self

    def set_alive(self, coords: list):
        for row, col in coords:
            self.board[row][col] = Cell(ALIVE)
            self.prev_board[row][col] = Cell(ALIVE)
        return self

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

    @property
    def list_of_values(self):
        """
        List of integer values - 1 ALIVE, 0 - DEAD
        """
        result = []
        for row in self.prev_board:
            result.append([cell.state for cell in row])
        return result

    def __str__(self):
        result = ''
        for row in self.prev_board:
            for cell in row:
                result += 'x' if cell.state == ALIVE else 'o'
            result += '\n'
        return result

    def __getitem__(self, item):
        row, col = item[0], item[1]
        if row < 0 or row > len(self.prev_board) - 1:
            return Cell(None)
        if col < 0 or col > len(self.prev_board) - 1:
            return Cell(None)
        try:
            return self.prev_board[row][col]
        except IndexError:
            traceback.print_exc()
            print('Row {} col {}'.format(row, col))

    def __setitem__(self, key, value):
        row, cell = key[0], key[1]
        self.board[row][cell] = value


if __name__ == '__main__':
    init_config = [(1, 1), (0, 1)]
    board = Board(3)
    board.set_alive(init_config)
    board.update()
    print(board)