import pygame


class Lives:
    """Track and draw how many lives the player has left."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.lives_left = self.settings.ship_limit
        self.font = pygame.font.SysFont(None, 40)

    def lose_life(self):
        """Take one life away. Return True if no lives are left."""
        self.lives_left -= 1
        return self.lives_left <= 0

    def reset_lives(self):
        self.lives_left = self.settings.ship_limit

    def draw_lives(self):
        text = "Lives: " + str(self.lives_left)
        text_picture = self.font.render(text, True, (0, 0, 0))
        text_rect = text_picture.get_rect()
        text_rect.topright = (self.settings.screen_width - 20, 20)
        self.screen.blit(text_picture, text_rect)