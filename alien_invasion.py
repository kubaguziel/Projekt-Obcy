import sys
import pygame 

from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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

        elif event.key == pygame.K_SPACE:
        #wystrzelenie pocisku
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """Reakcja na zwolnienie klawisza"""
        if event.key == pygame.K_RIGHT:                  
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)    

    def _update_bullets(self):
        """Uaktualnienie pocisków na i usunięcie tych niewidocznych na ekranie."""
        #uaktualnienie położenia pocisków
        self.bullets.update()

        #usunięcie pocisków, które znajdują się poza ekranem.
        for bullet in self.bullets.copy():      #musimy zrobić kopię grupy, ponieważ nie możemy usunąć elementó z listy podczas iteracji pętli przez tą listę
            if bullet.rect.bottom <=10:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
         #Odświeżanie ekranu w trakcie każdej iteracji pętli
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites(): #lista wszystkich pocisków w grupie Sprites
                bullet.draw_bullet()

            #wyświetlanie ostatnio zmodyfikowanego ekranu
            pygame.display.flip()

if __name__ == '__main__':
    #utworzenie egzemlarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()