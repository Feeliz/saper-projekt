from enum import Enum
import pygame as pg
from board import Board

FPS = 60

# TODO tutaj wczytać wszystkie obrazki


class MouseClick(Enum):
    LMB = 1  # lewy przycisk myszy
    RMB = 2  # prawy przycisk myszy


class Game:
    """ Klasa gry - posiada planszę i umożliwią interakcję z nią poprzez interfejs graficzny """

    def __init__(self, surface, width, height, mine_count):
        self.surface = surface
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
