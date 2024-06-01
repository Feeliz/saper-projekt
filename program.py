from enum import Enum
import pygame as pg
from game import Game
from button import Button
import config

# obrazki do menu
img_background = pg.image.load("images/main_menu/background.png")
img_easy_button = pg.image.load("images/main_menu/easy_button.png")
img_medium_button = pg.image.load("images/main_menu/medium_button.png")
img_hard_button = pg.image.load("images/main_menu/hard_button.png")


class Program:
    """ Klasa programu - zarządza menu głównym oraz odpala gry """

    def __init__(self):
        pg.init()
        self.screen = None
        self.clock = pg.time.Clock()

        ...  # TODO

    def run_menu(self):
        """ Fukcja odpowiedzialna za główne menu.
        Zwraca "easy"/"medium"/"hard" - stopień trudności gry wybrany przez gracza """

        pg.display.set_caption(" --- Saper --- ")

        screen_centerx, screen_centery = self.screen.get_rect().center
        easy_button = Button(img_easy_button, (screen_centerx, screen_centery - 25))
        medium_button = Button(img_medium_button, (screen_centerx, screen_centery + 50))
        hard_button = Button(img_hard_button, (screen_centerx, screen_centery + 125))

        while True:
            self.screen.blit(img_background, (0, 0))

            easy_button.draw(self.screen)
            medium_button.draw(self.screen)
            hard_button.draw(self.screen)

            pg.display.flip()
            self.clock.tick(config.FPS)

            events = list(pg.event.get())
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            if easy_button.is_clicked(events):
                return "easy"
            elif medium_button.is_clicked(events):
                return "medium"
            elif hard_button.is_clicked(events):
                return "hard"

            self.clock.tick(config.FPS)

    def run(self):
        """ Funkcja zawierająca główną pętle programu """

        while True:
            self.screen = pg.display.set_mode(img_background.get_size())
            difficulty = self.run_menu()
            pg.display.quit()
            game = Game(*config.GAME_PARAMETERS[difficulty])
            game.run()
