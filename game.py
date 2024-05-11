from enum import Enum
import pygame as pg
from board import Board, BoardState
from button import Button
import config

# TODO tutaj wczytać obrazki do planszy i okienka po grze


class MouseClick(Enum):
    LMB = 1  # lewy przycisk myszy
    RMB = 2  # prawy przycisk myszy


class Game:
    """ Klasa gry - posiada planszę i umożliwią interakcję z nią poprzez interfejs graficzny """

    def __init__(self, width, height, mine_count):
        self.surface = pg.display.set_mode((config.TILE_SIZE * width, config.TILE_SIZE * height))
        self.board = Board(width, height, mine_count)
        self.clock = pg.time.Clock()

    def draw(self):
        """ Fukcja rysująca planszę """

        ...  # TODO

    def get_player_input(self):
        """ Funkcja wykrywająca wciśnięcie myszy przez gracza.
            Zwraca krotkę (MouseClick, position), jeżeli wykryto wejście, w przeciwnym wypadku None """

        ...  # TODO

    def run(self):
        """ Fukcja zawierającą główną pętlę gry """

        ...  # TODO

    def run_post_game(self, game_outcome):
        """ Funkcja odpalająca okienko końcowe po zakończeniu gry """

        ...  # TODO
