ALIVE = 1
DEAD = 0


class Cell:
    def __init__(self, state):
        self.state = state

    @property
    def is_alive(self) -> bool:
        return True if self.state is ALIVE else False

    def will_survive(self, neighbours):
        alive_neighbours = sum([neighbour for neighbour in neighbours if neighbour is not None])
        if self.state is DEAD and alive_neighbours == 3:
            return True
        if self.state is ALIVE and 2 <= alive_neighbours <= 3:
            return True
        return False

    def __str__(self):
        if self.state is None:
            return 'out of range'
        return 'o' if self.state != ALIVE else 'x'

    def __repr__(self):
        return self.__str__()