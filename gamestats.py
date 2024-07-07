class GameStats:
    """Monitorowanie danych statystycznych w grze AlienInvasion"""

    def __init__(self,ai_game) -> None:
        self.settings = ai_game.settings
        self.reset_stats()
        #uruchomienie gry "Inwazja obcych w stanie nieaktywnym"
        self.game_active = False

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry"""
        self.ships_left = self.settings.ship_limit
