import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, star_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = star_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start with a star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Start the star's exact horizontal position.
        self.x = float(self.rect.x)