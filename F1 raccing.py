import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
WIDTH = 800
HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the game
pygame.display.set_caption("F1 Racer Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the font for the score
font = pygame.font.SysFont(None, 25)

# Define the function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

# Define the F1 Racer class
class F1Racer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("f1_car.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Create a group for all sprites
all_sprites = pygame.sprite.Group()

# Create a group for all enemies
enemies = pygame.sprite.Group()

# Create the F1 Racer object
f1_racer = F1Racer()

# Add the F1 Racer object to the all_sprites group
all_sprites.add(f1_racer)

# Create 1 Enemy objects
for i in range(1):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Set the initial score to 0
score = 0

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Set the running flag to True
running = True

# Start the game loop
while running:
    # Set the frame rate
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running
    # Update all sprites
    all_sprites.update()

    # Check for collisions between the F1 Racer and enemies
    hits = pygame.sprite.spritecollide(f1_racer, enemies, False)
    if hits:
        running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw all sprites
    all_sprites.draw(screen)

    # Display the score
    display_score(score)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
