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

        # self.board[y][x] to True jeżeli pole na pozycji (y, x) posiada minę
        self.board = [[False for _ in range(width)] for _ in range(height)]

        # self.discovered[y][x] to True jeżeli pole na pozycji (y, x) zostało odkryte
        self.discovered = [[False for _ in range(width)] for _ in range(height)]

        # self.flag[y][x] to True jeżeli pole na pozycji (y, x) została położona flaga
        self.flag = [[False for _ in range(width)] for _ in range(height)]

    def place_mines(self, start_position):
        """ Funkcja rozstawiająca miny na planszy (z gwaracnją, że nie będzie miny na start_position ani dookoła) """

        ...  # TODO

    def uncover(self, position):
        """ Funkcja odkrywająca pole na danej pozycji, zwraca BoardState """

        ...  # TODO

    def get_mine_count(self, position):
        """ Funkcja zwracająca liczbe min dookoła pola na danej pozycji """

        ...  # TODO

    def place_flag(self, position):
        """ Fukcja stawiająca flagę na danej pozycji """

        ...  # TODO

    def get_neighbors(self, position):
        """ Funkcja pomocnicza zwracająca pozycje sąsiadów pola na danej pozycji """

        ...  # TODO

    def is_position_correct(self, position):
        """ Fukcja pomocnicza sprawdzająca czy dana pozycja nie wychodzi poza planszę """

        ...  # TODO
