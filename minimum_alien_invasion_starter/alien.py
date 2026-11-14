import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represent one alien in the fleet."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.Surface((self.settings.alien_width, self.settings.alien_height))
        self.image.fill(self.settings.alien_color)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.health = self.settings.alien_health

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)

class SecondAlien(Alien):
    """Represent a second type of alien in the fleet."""

    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.health = self.settings.second_alien_health
        self.image.fill(self.settings.second_alien_color)

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            return True
        else:
            self.image.fill(self.settings.second_alien_damaged_color)
            return False