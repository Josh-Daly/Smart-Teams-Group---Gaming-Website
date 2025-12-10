import pygame, random
CELL = 20

class Food:
    def __init__(self, color, cols, rows):
        self.color = color
        self.cols = cols
        self.rows = rows
        self.relocate()

    def relocate(self):
        self.pos = (random.randint(0, self.cols - 1), random.randint(0, self.rows - 1))

    def draw(self, screen):
        x, y = self.pos
        pygame.draw.rect(screen, self.color, (x * CELL, y * CELL, CELL, CELL))
