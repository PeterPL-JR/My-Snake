import pygame
import random

IS_GRASS_ITEM = 1

# Initialize terrain
def init_terrain():
    import snake

    for x in range(0, snake.MAP_SIZE):
        for y in range(0, snake.MAP_SIZE):
            snake.map_tiles.append(Tile(x, y, snake.screen))

# Render terrain
def render_terrain():
    import snake

    for tile in snake.map_tiles:
        tile.render()

def rand_apple(screen):
    return Apple(screen)

def take_apple(snake_object):
    import snake
    
    snake_object.points += 1
    snake.apple = rand_apple(snake_object.screen)

class Image_Asset:
    def __init__(self, path):
        self.img = pygame.image.load(path)

    def render(self, x, y, width, height, screen):
        rendered_img = pygame.transform.scale(self.img, (width, height))
        screen.blit(rendered_img, (x, y))
    
    def render_rotated(self, x, y, width, height, angle, screen):
        rendered_img = pygame.transform.scale(self.img, (width, height))
        rendered_img = pygame.transform.rotate(rendered_img, angle)
        screen.blit(rendered_img, (x, y))

# Tiles images
grass_tex_1 = Image_Asset("Textures/tex_grass_1.png")
grass_tex_2 = Image_Asset("Textures/tex_grass_2.png")
apple_tex = Image_Asset("Textures/tex_apple.png")

class Tile:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.item = random.randint(0, IS_GRASS_ITEM) == IS_GRASS_ITEM
        self.screen = screen

    def render(self):
        from snake import F_SIZE

        rendering_x = self.x * F_SIZE
        rendering_y = self.y * F_SIZE
        grass_tex_1.render(rendering_x, rendering_y, F_SIZE, F_SIZE, self.screen)

        if self.item:
            grass_tex_2.render(rendering_x, rendering_y, F_SIZE, F_SIZE, self.screen)

class Apple:
    def __init__(self, screen):
        from snake import MAP_SIZE

        self.screen = screen
        self.x = random.randint(0, MAP_SIZE - 1)
        self.y = 3

    def rand_pos():
        from snake import MAP_SIZE

        x_pos = random.randint(0, MAP_SIZE - 1)
        y_pos = random.randint(0, MAP_SIZE - 1)

        return (x_pos, y_pos)
    
    def render(self):
        from snake import F_SIZE

        render_x = self.x * F_SIZE
        render_y = self.y * F_SIZE

        apple_tex.render(render_x, render_y, F_SIZE, F_SIZE, self.screen)