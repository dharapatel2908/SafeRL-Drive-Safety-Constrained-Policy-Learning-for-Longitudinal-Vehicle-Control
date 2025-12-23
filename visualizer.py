import pygame

WIDTH, HEIGHT = 800, 200

class CarVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RL Self-Driving Demo")
        self.clock = pygame.time.Clock()

    def draw(self, ego_x, front_x):
        self.screen.fill((30, 30, 30))

        # Ego car (blue)
        pygame.draw.rect(
            self.screen, (0, 120, 255),
            pygame.Rect(ego_x, HEIGHT // 2, 50, 30)
        )

        # Front car (red)
        pygame.draw.rect(
            self.screen, (255, 80, 80),
            pygame.Rect(front_x, HEIGHT // 2, 50, 30)
        )

        pygame.display.flip()
        self.clock.tick(30)

    def close(self):
        pygame.quit()
