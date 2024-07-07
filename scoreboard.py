import pygame.font

class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji na temat punktacji"""
    def __init__(self, ai_game):
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

    def check_high_score(self):
        """Sprawdzenie, czy mamy nowy najlepszy wynik"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Wyświetlanie punktacji na ekranie"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)