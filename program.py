from enum import Enum
import pygame as pg
import config


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

        ...  # TODO


class Button:
    """ Klasa przycisku - posiada obrazek oraz pozycję"""

    def __init__(self, image, position):
        self.image = image
        self.position = position

        y, x = position
        dy = y - image.get_width() * (config.BUTTON_HOVER_SCALING - 1) / 2
        dx = x - image.get_width() * (config.BUTTON_HOVER_SCALING - 1) / 2
        self.image_on_hover = pg.transform.scale_by(image, config.BUTTON_HOVER_SCALING)
        self.position_on_hover = (y - dy, x - dx)

        self.rect = pg.Rect(position, image.get_size())

    def is_hovered(self):
        """ Funkcja sprawdzająca, czy najechano myszą na przycisk """

        ...  # TODO

    def is_clicked(self):
        """ Funkcja sprawdzająca, czy wcziśnięto przycisk """

        ...  # TODO

    def draw(self, surface):
        """ Funkcja rysująca przycisk na daną powierzchnię """

        ...  # TODO
