import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants (window size and speed)
CELL = 20  # Size of each square
COLS, ROWS = 32, 24  # Grid size
W, H = COLS * CELL, ROWS * CELL
FPS = 10  # Frames per second (snake speed)

# Create game window
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Two Player Snake Game")

# Colors
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

# Create a clock to control speed
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self, color, start_pos, direction):
        self.body = [start_pos]
        self.color = color
        self.direction = direction
        self.grow = False

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction 
        new_head = ((x + dx) % COLS, (y + dy) % ROWS)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self):
        for (x, y) in self.body:
            pygame.draw.rect(screen, self.color, (x * CELL, y * CELL, CELL, CELL))

    def check_self_collision(self):
        return self.body[0] in self.body[1:]

# Food function
def spawn_food():
    return (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))

# Game setup
snake1 = Snake(CYAN, (5, 5), (1, 0))  # Player 1 starts at left
snake2 = Snake(ORANGE, (25, 18), (-1, 0))  # Player 2 starts at right
food = spawn_food()

# Main loop
while True:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Player controls
    keys = pygame.key.get_pressed()
    # Player 1 - WASD
    if keys[pygame.K_w]: snake1.direction = (0, -1)
    if keys[pygame.K_s]: snake1.direction = (0, 1)
    if keys[pygame.K_a]: snake1.direction = (-1, 0)
    if keys[pygame.K_d]: snake1.direction = (1, 0)
    # Player 2 - Arrow keys
    if keys[pygame.K_UP]: snake2.direction = (0, -1)
    if keys[pygame.K_DOWN]: snake2.direction = (0, 1)
    if keys[pygame.K_LEFT]: snake2.direction = (-1, 0)
    if keys[pygame.K_RIGHT]: snake2.direction = (1, 0)

    # 3. Move snakes
    snake1.move()
    snake2.move()

    # 4. Check if they eat food
    for snake in [snake1, snake2]:
        if snake.body[0] == food:
            snake.grow = True
            food = spawn_food()

    # 5. Check for collisions
    if snake1.check_self_collision() or snake1.body[0] in snake2.body:
        print("Player 2 wins!")
        pygame.quit()
        sys.exit()

    if snake2.check_self_collision() or snake2.body[0] in snake1.body:
        print("Player 1 wins!")
        pygame.quit()
        sys.exit()

    # 6. Draw everything
    screen.fill(BLACK)
    snake1.draw()
    snake2.draw()
    pygame.draw.rect(screen, RED, (food[0] * CELL, food[1] * CELL, CELL, CELL))
    pygame.display.flip()

    # 7. Control game speed
    clock.tick(FPS)
