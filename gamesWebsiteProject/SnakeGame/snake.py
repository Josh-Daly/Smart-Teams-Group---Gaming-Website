import pygame
CELL = 20

class Snake:
    def __init__(self, color, start_pos, direction, controls):
        self.color = color
        self.body = [start_pos]
        self.direction = direction
        self.controls = controls
        self.grow = 0
        self.alive = True

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.controls['up'] and self.direction != (0, 1):
                self.direction = (0, -1)
            elif event.key == self.controls['down'] and self.direction != (0, -1):
                self.direction = (0, 1)
            elif event.key == self.controls['left'] and self.direction != (1, 0):
                self.direction = (-1, 0)
            elif event.key == self.controls['right'] and self.direction != (-1, 0):
                self.direction = (1, 0)

    def move(self, cols, rows):
        if not self.alive:
            return
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = ((x + dx) % cols, (y + dy) % rows)
        if new_head in self.body:
            self.alive = False
        self.body.insert(0, new_head)
        if self.grow > 0:
            self.grow -= 1
        else:
            self.body.pop()

    def draw(self, screen):
        for (x, y) in self.body:
            pygame.draw.rect(screen, self.color, (x * CELL, y * CELL, CELL, CELL))
