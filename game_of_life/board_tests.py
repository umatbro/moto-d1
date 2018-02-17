import unittest
from game_of_life.board import Board
from game_of_life.cell import Cell, ALIVE, DEAD


def create_test_board(size):
    board = Board(size)
    board[0, 0].state = ALIVE
    board[0, 1].state = ALIVE
    board[2, 1].state = ALIVE
    return board


class BoardTests(unittest.TestCase):
    def test_get_neighbours(self):
        board = create_test_board(3)
        self.assertListEqual(board.get_neighbour_states(1, 0), [
            None, None, ALIVE,
            ALIVE, DEAD,
            ALIVE, DEAD, None
        ])

    def test_simple_update(self):
        alive_cells = [(0, 0), (1, 1), (0, 1)]
        board = Board(3)
        board.set_alive_cells(alive_cells)
        board.update()
        states = board.list_of_values
        self.assertListEqual(states, [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ])

    def test_simple_update2(self):
        init_config = [(0, 0), (0, 1), (0, 2)]
        board = Board(3)
        board.set_alive_cells(init_config)
        board.update()
        states = board.list_of_values
        self.assertListEqual(states, [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])

    def test_overpopulation(self):
        init_config = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]
        board = Board(3)
        board.set_alive_cells(init_config)
        board.update()
        states = board.list_of_values
        self.assertListEqual(states, [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])


class CellTest(unittest.TestCase):
    def test_is_alive(self):
        alive_cell = Cell(ALIVE)
        self.assertTrue(alive_cell.is_alive)

        dead_cell = Cell(DEAD)
        self.assertFalse(dead_cell.is_alive)

    def test_create_life(self):
        cell = Cell(DEAD)
        neighbours = [1, 1, 1, 0, 0, 0, 0, None, None]
        self.assertTrue(cell.will_survive(neighbours))

    def test_will_not_be_born(self):
        cell = Cell(DEAD)
        neighbours = [1, 1, 0, 0, 0, 0, 0,]
        self.assertFalse(cell.will_survive(neighbours))
        neighbours = [1, 1, 1, 1, 0, 0, 0]
        self.assertFalse(cell.will_survive(neighbours))

    def test_stay_alive(self):
        cell = Cell(ALIVE)
        neighbours2 = [1, 1, 0, 0, 0, 0, None, None]
        self.assertTrue(cell.will_survive(neighbours2))
        neighbours3 = [1, 1, 1, 0, 0, 0, None, None]
        self.assertTrue(cell.will_survive(neighbours3))

    def test_will_not_survive_overpopulation(self):
        cell = Cell(ALIVE)
        neighbours = [1, 1, 1, 1, 0, 0, 0, 0]
        self.assertFalse(cell.will_survive(neighbours))

    def test_will_not_survive_underpopulation(self):
        cell = Cell(ALIVE)
        neighbours = [1, 0, 0, 0, 0, 0, 0]
        self.assertFalse(cell.will_survive(neighbours))


if __name__ == '__main__':
    unittest.main()
