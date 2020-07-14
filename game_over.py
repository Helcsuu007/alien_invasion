import pygame.font

class GameOver:

    def __init__(self, ai_game, go_msg):
        """Initialize Game Over screen attributes."""
        self.screen = ai_game.screen
        self.go_screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the screen.
        self.width, self.height = 800, 600
        self.background_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 90)

        # Build the game over screen's rect object and position it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.go_screen_rect.center

        # The game over message's preparation.
        self._prep_go_msg(go_msg)

    def _prep_go_msg(self, go_msg):

        self.go_msg_image = self.font.render(go_msg, True, self.text_color,
                self.background_color)
        self.go_msg_image_rect = self.go_msg_image.get_rect()
        self.go_msg_image_rect.center = self.go_screen_rect.center

    def draw_go_screen(self):
        # Draw blank screen, then draw the game over message.
        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.go_msg_image, self.go_msg_image_rect)