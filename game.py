from enum import Enum
import pygame as pg
from board import Board, BoardState
from button import Button
import config

img_bomb = pg.image.load("images/tiles/bomb.png")
img_covered = pg.image.load("images/tiles/covered.png")
img_flag = pg.image.load("images/tiles/flag.png")
imgs_uncovered = [pg.image.load(f"images/tiles/uncovered_{x}.png") for x in range(9)]


class Game:
    """ Klasa gry - posiada planszę i umożliwią interakcję z nią poprzez interfejs graficzny """

    def __init__(self, width, height, mine_count):
        self.surface = pg.display.set_mode((config.TILE_SIZE * width, config.TILE_SIZE * height))
        self.board = Board(width, height, mine_count)
        self.running = True
        self.clock = pg.time.Clock()

    @staticmethod
    def into_board_position(position):
        """ Funkcja konwertująca pozycje w pikselach na pozycje na gridzie """

        y, x = position
        return y // config.TILE_SIZE, x // config.TILE_SIZE

    def process_input(self):
        """ Funkcja reagująca na wejście gracza """

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                screen_x, screen_y = pg.mouse.get_pos()
                y, x = self.into_board_position((screen_y, screen_x))
                if event.button == 1:  # LMB
                    self.board.uncover((y, x))
                elif event.button == 3:  # RMB
                    self.board.set_flag((y, x))

    def get_image(self, position):
        """ Funkcja pomocnicza zwracająca odpowiedni obrazek do pola o danej pozycji """

        y, x = position
        if not self.board.uncovered[y][x]:
            if self.board.flag[y][x]:
                return img_flag
            return img_covered

        if self.board.bomb[y][x]:
            return img_bomb

        bomb_count = self.board.get_mine_count(position)
        return imgs_uncovered[bomb_count]

    def draw(self):
        """ Fukcja rysująca planszę """

        for y in range(self.board.height):
            for x in range(self.board.width):
                screen_x, screen_y = config.TILE_SIZE * x, config.TILE_SIZE * y
                image = self.get_image((y, x))
                self.surface.blit(image, image.get_rect(topleft=(screen_x, screen_y)))

    def run(self):
        """ Fukcja zawierającą główną pętlę gry """

        while self.running:  # TODO troche pozmieniać
            self.draw()

            pg.display.update()
            self.clock.tick(config.FPS)
            self.process_input()

    def run_post_game(self, game_outcome):
        """ Funkcja odpalająca okienko końcowe po zakończeniu gry """

        ...  # TODO
