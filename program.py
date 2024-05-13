from enum import Enum
import pygame as pg
from game import Game
from button import Button
import config

# TODO tutaj wczytać obrazki do menu


class Program:
    """ Klasa programu - zarządza menu głównym oraz odpala gry """

    def __init__(self):
        self.screen = pg.display.set_mode(config.MENU_SCREEN_SIZE)
        self.clock = pg.time.Clock()

        ...  # TODO

    def run_menu(self):
        """ Fukcja odpowiedzialna za główne menu.
        Zwraca "easy"/"medium"/"hard" - stopień trudności gry wybrany przez gracza """

        ...  # TODO

    def run(self):
        """ Funkcja zawierająca główną pętle programu """

        game = Game(10, 10, 20)  # TODO TYMCZASOWE !!!
        game.run()

        ...  # TODO
