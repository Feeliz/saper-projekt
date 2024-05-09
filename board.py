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

        # self.flag[y][x] to True jeżeli pole na pozycji (y, x) została położona flags
        self.flag = [[False for _ in range(width)] for _ in range(height)]

    def place_mines(self, start_position):
        """ Funkcja rozstawiająca miny na planszy (z gwaracnją, że nie będzie miny na start_position """

        ...  # TODO

    def uncover(self, position):
        """ Funkcja odkrywająca pole na pozycji position
            zwraca False jeżeli odkryto minę, w przeciwnym wypadrku True """

        ...  # TODO

    def get_mine_count(self, position):
        """ Funkcja zwracająca liczbe min dookoła pola na pozycji position """

        ...  # TODO
