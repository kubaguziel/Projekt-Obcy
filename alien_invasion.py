import sys
import pygame 

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""
    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_width = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obcych")

        self.ship = Ship(self)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    def _check_events(self):
        #oczekiwanie na naciśnięcie klawisza lub przycisku myszy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
        
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                     
    def _check_keydown_events(self,event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_RIGHT:
        #przesunięcie statku w prawą stronę
           self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:                          
        #przesuniecie statku w lewą stronę
            self.ship.moving_left = True

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self,event):
        """Reakcja na zwolnienie klawisza"""
        if event.key == pygame.K_RIGHT:                  
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
         #Odświeżanie ekranu w trakcie każdej iteracji pętli
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #wyświetlanie ostatnio zmodyfikowanego ekranu
            pygame.display.flip()

if __name__ == '__main__':
    #utworzenie egzemlarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()