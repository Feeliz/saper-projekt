import time
import pygame as pg
from board import Board, BoardState
from button import Button
import config

# obrazki do gry
img_bomb = pg.image.load("images/tiles/bomb.png")
img_covered = pg.image.load("images/tiles/covered.png")
img_flag = pg.image.load("images/tiles/flag.png")
imgs_uncovered = [pg.image.load(f"images/tiles/uncovered_{x}.png") for x in range(9)]

# obrazki do menu
img_win = pg.image.load("images/end_menu/end_win.png")
img_defeat = pg.image.load("images/end_menu/end_defeat.png")
img_ok_button = pg.image.load("images/end_menu/ok_button.png")
scale = 0.6
img_win = pg.transform.scale(img_win,
                       (int(img_win.get_width() * scale), int(img_win.get_height() * scale)))
img_defeat = pg.transform.scale(img_defeat,
                          (int(img_defeat.get_width() * scale), int(img_defeat.get_height() * scale)))
img_ok_button = pg.transform.scale(img_ok_button,
                             (int(img_ok_button.get_width() * scale), int(img_ok_button.get_height() * scale)))


class Game:
    """ Klasa gry - posiada planszę i umożliwią interakcję z nią poprzez interfejs graficzny """

    def __init__(self, size, mine_count):
        width, height = size
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
        """ Funkcja reagująca na wejście gracza, zwraca obecny stan gry """

        state = BoardState.PLAYING
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                screen_x, screen_y = pg.mouse.get_pos()
                y, x = self.into_board_position((screen_y, screen_x))
                if event.button == 1:  # LMB
                    state = self.board.uncover((y, x))
                elif event.button == 3:  # RMB
                    self.board.set_flag((y, x))

        return state

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

        state = BoardState.PLAYING
        while self.running and state == BoardState.PLAYING:
            state = self.process_input()

            self.draw()
            pg.display.update()
            pg.display.set_caption(f"{self.board.safe_tile_count - self.board.counter}/{self.board.safe_tile_count}")
            self.clock.tick(config.FPS)

        # jeżeli gra się normalnie zakończyła (użytkownik nie wyszedł X-em), to odpal okienko po grze
        if state != BoardState.PLAYING:
            time.sleep(config.END_MENU_DELAY)
            self.run_post_game(state)

        pg.display.quit()

    def run_post_game(self, game_outcome):
        """ Funkcja odpalająca okienko końcowe po zakończeniu gry """

        base_img = img_win if game_outcome == BoardState.WIN else img_defeat
        base_rect = base_img.get_rect()
        screen_centerx, screen_centery = self.surface.get_rect().center
        base_rect.center = (screen_centerx, screen_centery)

        ok_button = Button(img_ok_button, (screen_centerx, screen_centery + 20))

        self.running = True
        while self.running:
            self.surface.blit(base_img, base_rect)
            ok_button.draw(self.surface)
            pg.display.update()

            events = list(pg.event.get())
            for event in events:
                if event.type == pg.QUIT or ok_button.is_clicked(events):
                    pg.display.quit()
                    self.running = False
                    break

            self.clock.tick(config.FPS)
