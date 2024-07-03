import pygame
from pygame.sprite import Sprite #kiedy używamy sprite'ów możemy grupować ze sobą powiązane elementy i przeprowadzać operacje na całej grupie elementów

class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez statek"""
    def __init__(self, ai_game): #ai_game to aktualny egzemplarz klasy AlienInvasion
        """Utworzenie obiektu pocisku w aktualnym miejscu położenia statku"""
        super().__init__() #prawidłowe dziedziczenie po sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Utworzenie prostokąta pocisku w punkcie (0,0), a następnie
        # zdefiniowanie dla niego odpowiedniego położenia.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej
        self.y = float(self.rect.y)

    def update(self):
        """Poruszanie pociskiem po ekranie"""
        #uaktualnianie położenia pocisku
        self.y -= self.settings.bullet_speed
        #uaktualnianie położenia pocisku na ekranie.
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyświetlenie pocisku na ekranie."""
        pygame.draw.rect(self.screen,self.color,self.rect)
