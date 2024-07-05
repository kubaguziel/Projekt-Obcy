import pygame
from settings import Settings

class Ship:
    """Klasa przeznaczona do zarządzania statkiem kosmicznym"""
    def __init__(self, ai_game) -> None: #ai_game to odniesienie do aktualnego egzemplarza klasy AlienInvasion
        """Inicjalizacja statku kosmicznego i jego położenie poczatkowe"""
        self.screen = ai_game.screen #przypisanie ekranu do obiektu klasy Ship, żeby był do nich łatwy dostęp w całej klasie
        self.screen_rect = ai_game.screen.get_rect() #dzięki temu statek kosmiczny zostaje umieszczony w odpowiednim miejscu na ekranie

        self.settings = Settings()

        #Wczytanie obrazu statku kosmicznego
        self.image = pygame.image.load('images/ship.bmp') 
        self.rect = self.image.get_rect()

        #Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        #Położenie posiome statku jest przechowywane w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)

        #Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnianie położenia statku"""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #uaktualnienie obiektu rect na podstawie wartości self.x
        self.rect.x = self.x


    def blitme(self):
        """Wyświetlenie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczenie statku na środku przy dolnej krawędzi ekranu"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)