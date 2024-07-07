import pygame
class Settings:
    """Klasa przeznaczona do przechowywania ustawień"""
    def __init__(self) -> None:
        #ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #ustawienia statku
        self.ship_limit = 3
        #ustawienia dotyczące pocisku
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #ustawienia obcych
        self.fleet_drop_speed = 10
        
        #zmiana szybkości gry
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5

        #wartość fleet_direction 1 oznacza w prawo, -1 oznacza w lewo
        self.fleet_direction = 1

    def increase_speed(self):
        """Przyspieszenie rozgrywki"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale