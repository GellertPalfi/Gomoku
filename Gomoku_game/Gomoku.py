import pygame

ROWS = 19
COLS = 19


class Colors:
    BLACK = 0, 0, 0
    WHITE = 200, 200, 200
    ORANGE = 255, 127, 80
    BROWN = 205, 128, 0


class Gomoku:
    def __init__(self, size=50) -> None:
        self.size = size
        self.cols = COLS
        self.rows = ROWS
        self.width = COLS * size
        self.height = ROWS * size
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_background(self):
        rect = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(self.screen, Colors.BROWN, rect)

    def row_lines(self):
        pass

    def draw_lines(self):
        pygame.draw.line(
            self.screen, Colors.BLACK, (0, self.size), (self.width, self.size)
        )

    def play(self):
        running = True
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_background()
            self.draw_lines()
            pygame.display.update()
