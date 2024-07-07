import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji na temat punktacji"""
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #ustawienia czcionki dla punktacji
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #przygotowanie początkowych obrazów z punktacją
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Przekształcenie punktacji na obraz"""
        score_str = "Wynik: "
        score_str += str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        #wyświetlenie punktacji w prawym górnym rogu ekranu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

    def prep_high_score(self):
        """Przekształcenie najlepszego wyniku na obraz"""
        high_score = self.stats.high_score
        high_score_str = "Najlepszy wynik: "
        high_score_str += "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        #wyąwietlanie najlepszego wyniku na środku ekranu przy górnej krawędzi
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Konwersja numeru poziomu na obrazek."""
        level = self.stats.level
        level_str = "Level: "
        level_str += str(level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        #numer poziomu wyświetlany pod high_score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.high_score_rect.right
        self.level_rect.top = self.high_score_rect.bottom + 10 
    
    def prep_ships(self):
        """Wyświetla liczbę statków, jakie zostały graczowi"""
        self.ships = Group() #tworzymy pustą grupę o nazwie self.ships do przechowywania egzemplarzy statku
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game) 
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        

    def check_high_score(self):
        """Sprawdzenie, czy mamy nowy najlepszy wynik"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Wyświetlanie punktacji na ekranie"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)