import pygame as pg
import config


class Button:
    """ Klasa przycisku - posiada obrazek oraz pozycję"""

    def __init__(self, image, position):
        self.image = image
        self.position = position

        self.image_on_hover = pg.transform.scale_by(image, config.BUTTON_HOVER_SCALING)
        self.hitbox = pg.Rect((0, 0), image.get_size())
        self.hitbox.center = position

    def is_hovered(self):
        """ Funkcja sprawdzająca, czy najechano myszą na przycisk """

        mouse_pos = pg.mouse.get_pos()
        return self.hitbox.collidepoint(mouse_pos)

    def is_clicked(self, events):
        """ Funkcja sprawdzająca, czy wciśnięto przycisk """

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered():  # LMB
                return True

        return False

    def draw(self, surface):
        image = self.image if not self.is_hovered() else self.image_on_hover
        image_rect = image.get_rect()
        image_rect.center = self.position
        surface.blit(image, image_rect)
