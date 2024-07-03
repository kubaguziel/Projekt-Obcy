class Settings:
    """Klasa przeznaczona do przechowywania ustawień"""
    def __init__(self) -> None:
        #ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ustawienia statku
        self.ship_speed = 1.5
