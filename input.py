import pygame

DIR_LEFT = 0
DIR_RIGHT = 1

DIR_UP = 2
DIR_DOWN = 3

def key_down(key):
    import snake

    # Player move up
    if(key == pygame.K_w):
        snake.player_snake.move(DIR_UP)

    # Player move down
    if(key == pygame.K_s):
        snake.player_snake.move(DIR_DOWN)

    # Player move left
    if(key == pygame.K_a):
        snake.player_snake.move(DIR_LEFT)

    # Player move right
    if(key == pygame.K_d):
        snake.player_snake.move(DIR_RIGHT)

def mouse_clicked(button):
    import snake
    if(button == pygame.BUTTON_LEFT and snake.game_over):
        snake.reset()