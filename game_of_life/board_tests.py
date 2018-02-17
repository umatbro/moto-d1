import unittest
from game_of_life.board import Board
from game_of_life.cell import Cell, ALIVE, DEAD


def create_test_board(size):
    board = Board(size)
    board[0, 0].state = ALIVE
    board[0, 1].state = ALIVE
    board[2, 1].state = ALIVE
    return board


class BoardTest(unittest.TestCase):
    def test_get_neighbours(self):
        board = create_test_board(3)
        self.assertListEqual(board.get_neighbour_states(1, 0), [
            None, None, ALIVE,
            ALIVE, DEAD,
            ALIVE, DEAD, None
        ])

    def test_simple_update(self):
        init_config = [(0, 0), (1, 1), (0, 1)]
        board = Board(3)
        board.set_alive(init_config)
        board.update()
        states = board.list_of_values
        self.assertEqual(states, [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ])


class CellTest(unittest.TestCase):
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