import random
from enum import Enum


class BoardState(Enum):
    PLAYING = 1  # gra się jeszcze nie skończyła
    WIN = 2      # gracz wygrał (wszystkie pola nieposiadające miny zostały odkryte)
    LOSS = 3     # gracz przegrał (zostało odkryte pole z miną)


class Board:
    """ Klasa planszy - posiada szerokość, wysokość i ustaloną liczbę min """

    def __init__(self, width, height, mine_count):
        self.width = width
        self.height = height
        self.mine_count = mine_count

        # self.bomb[y][x] to True jeżeli pole na pozycji (y, x) posiada minę
        self.bomb = [[False for _ in range(width)] for _ in range(height)]

        # self.flag[y][x] to True jeżeli pole na pozycji (y, x) została położona flaga
        self.flag = [[False for _ in range(width)] for _ in range(height)]

        # self.uncovered[y][x] to True jeżeli pole na pozycji (y, x) zostało odkryte
        self.uncovered = [[False for _ in range(width)] for _ in range(height)]

    def place_mines(self, start_position):
        """ Funkcja rozstawiająca miny na planszy (z gwaracnją, że nie będzie miny na start_position ani dookoła) """

        candidates = {(y, x) for x in range(self.height) for y in range(self.width)}
        safe_tiles = {start_position} | set(self.get_neighbors(start_position))
        candidates -= safe_tiles  # wyklucz startowe pola z puli możliwych pozycji bomb

        mine_positions = random.sample(candidates, self.mine_count)
        for y, x in mine_positions:
            self.bomb[y][x] = True

    def uncover(self, position):
        """ Funkcja odkrywająca pole na danej pozycji, zwraca BoardState """

        y, x = position
        if self.flag[y][x]:  # jeżeli pole jest zaflagowane, to nie odkrywaj
            return

        self.uncovered[y][x] = True
        if self.bomb[y][x]:
            return BoardState.LOSS

        # jeżeli żaden z sąsiadów nie posiada bomby, to rekurencyjnie je odkryj
        if self.get_mine_count(position) == 0:
            for neighbor_position in self.get_neighbors(position):
                new_y, new_x = neighbor_position
                if not self.uncovered[new_y][new_x]:
                    self.uncover(neighbor_position)

    def get_mine_count(self, position):
        """ Funkcja zwracająca liczbe min dookoła pola na danej pozycji """

        count = 0
        for y, x in self.get_neighbors(position):
            if self.bomb[y][x]:
                count += 1

        return count

    def set_flag(self, position):
        """ Fukcja stawiająca lub usuwająca flagę na danej pozycji """

        y, x = position
        if not self.uncovered[y][x]:
            self.flag[y][x] = not self.flag[y][x]

    def get_neighbors(self, position):
        """ Funkcja pomocnicza zwracająca pozycje sąsiadów pola na danej pozycji """

        y, x = position
        neighbors = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                new_position = (y + dy, x + dx)
                if new_position != position and self.is_position_correct(new_position):
                    neighbors.append(new_position)

        return neighbors

    def is_position_correct(self, position):
        """ Fukcja pomocnicza sprawdzająca czy dana pozycja nie wychodzi poza planszę """

        y, x = position
        return 0 <= x < self.width and 0 <= y < self.height
