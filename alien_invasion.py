import sys
from time import sleep
import pygame 

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gamestats import GameStats

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

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()

            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
        #print(len(self.bullets))
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Metoda sprawdzająca czy nastąpiła kolizja pocisku z obcym"""
        #sprawdzenie, czy którykolwiek pocisk trafił obcego
        #jeśeli tak, usuwamy zarówno pocisk, jak i obcego
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,True,True)
        if len(self.aliens) == 0:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Utworzenie pełnej floty obcych"""
        #utworzenie obcego i ustalenie liczby obych, którzy mieszczą się w rzędzie
        #odległość pomiędzy obcymi jest równa szerokości obcego
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (alien_width-2)

        #ustalenie ile rzędów obcych zmieści się na ekranie
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)
        
        for row_number in range(number_rows-1):
            for alien_number in range(number_aliens_x):
                #utworzenie obcego i umieszczenie go w rzędzie
                self._create_alien(alien_number,row_number)

    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Funkcja sprawdzająca czy statek został uderzony"""
        if(self.stats.ships_left > 0):
            #Zmniejszenie wartości dostępnych statków
            self.stats.ships_left -= 1
            #Usunięcie zawartości list aliens i bullets
            self.aliens.empty()
            self.bullets.empty()
            #Utworzenie nowej floty i wyśrodkowanie statku
            self._create_fleet()
            self.ship.center_ship()
            #Pauza
            sleep(1)
            #zmieniamy gre na nieaktywną
        else:    
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Funkcja sprawdzająca czy kosmici nie dotknęli dolnej krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #to samo co w przypadku zderzenia ze statkiem
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Przesunięcie całej floty w doł i zmiana kierunku, w którym się porusza."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
         #Odświeżanie ekranu w trakcie każdej iteracji pętli
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites(): #lista wszystkich pocisków w grupie Sprites
                bullet.draw_bullet()

            self.aliens.draw(self.screen) #argumentem funkcji draw jest powierzchnia, na której mają być umieszczone obiekty

            #wyświetlanie ostatnio zmodyfikowanego ekranu
            pygame.display.flip()


if __name__ == '__main__':
    #utworzenie egzemlarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()