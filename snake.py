import pygame, sys
import input

from player import Snake
import terrain

# Screen constants
F_SIZE = 50 # Field size
MAP_SIZE = 12 # Map size
S_SIZE = F_SIZE * MAP_SIZE # Width/Height of the screen

# Screen
screen = pygame.display.set_mode((S_SIZE, S_SIZE))
pygame.display.set_caption("My-Snake")

apple = terrain.rand_apple(screen) # Apple

player_snake = Snake(screen) # Player snake object
map_tiles = [] # Tiles

#Init
pygame.init()
terrain.init_terrain()

# Time variables
clock = pygame.time.Clock()
delta = 0.0
MAX_FPS = 4

# Update function
def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if(event.type == pygame.KEYDOWN):
            input.key_down(event.key)
    
    player_snake.update()

# Render function
def render():
    terrain.render_terrain()
    apple.render()
    player_snake.render()

    pygame.display.flip()

# Game loop
render()
while True:
    pygame.time.wait(int(1000 / MAX_FPS))
    update()
    render()