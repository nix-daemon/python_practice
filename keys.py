import pygame
import sys

class Keys:
    """Start Overall class to manage game assets and behavior"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Keys")
        self.bg_color = (255, 255, 255)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    key = Keys()
    key.run_game()