import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedyńczego obcego"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #umieszczenie nowego obcego w pobliżu lewego górnego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #przechowywanie dokładnego poziomego położenia obcego 
        self.x = float(self.rect.x)

    def check_edges(self):
        """Zwraca wartość True, jeśli obcy znajduje się przy krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Przesunięcie obcego w prawo lub lewo"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x