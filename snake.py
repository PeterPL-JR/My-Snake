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
icon = pygame.image.load("Textures/Snake/sk_head.png")
pygame.display.set_icon(icon)

player_snake = Snake(screen) # Player snake object
apple = terrain.rand_apple(player_snake) # Apple
map_tiles = [] # Tiles
game_over = False

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
        if(event.type == pygame.MOUSEBUTTONDOWN):
            input.mouse_clicked(event.button)
    
    player_snake.update()

# Render function
def render():
    terrain.render_terrain()
    apple.render()
    player_snake.render()
    render_gui()

    pygame.display.flip()

def render_gui():
    gui_img_size = int(F_SIZE * 1)
    gui_font_size = int(gui_img_size * 0.72)

    gui_img = icon
    gui_img = pygame.transform.scale(gui_img, (gui_img_size, gui_img_size))
    screen.blit(gui_img, (10, 10))

    gui_font = pygame.font.SysFont("Verdana", gui_font_size, True)
    gui_text = gui_font.render(str(player_snake.points), True, "white")
    screen.blit(gui_text, (gui_img_size * 1.2, 8))

    if(game_over):
        render_game_over()

def render_game_over():
    text_font = pygame.font.SysFont("Verdana", 80, True)
    text = text_font.render("Game over!", True, "white")
    text_rect = text.get_rect(center=(S_SIZE / 2, S_SIZE / 2))
    screen.blit(text, text_rect)

def reset():
    pass

# Game loop
render()
while True:
    pygame.time.wait(int(1000 / MAX_FPS))
    update()
    render()