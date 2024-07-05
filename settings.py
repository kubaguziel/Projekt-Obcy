import pygame
class Settings:
    """Klasa przeznaczona do przechowywania ustawień"""
    def __init__(self) -> None:
        #ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #ustawienia statku
        self.ship_speed = 1.5
        self.ship_limit = 3
        #ustawienia dotyczące pocisku
        self.bullet_speed = 1.5
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5
        #ustawienia obcych
        self.alien_speed = 0.8
        self.fleet_drop_speed = 5
        #wartość fleet_direction 1 oznacza w prawo, -1 oznacza w lewo
        self.fleet_direction = 1