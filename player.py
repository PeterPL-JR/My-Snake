import input
from terrain import Image_Asset

# Player images
sk_head_img = Image_Asset("Textures/Snake/sk_head.png")
sk_tail_img = Image_Asset("Textures/Snake/sk_tail.png")

sk_body_img_1 = Image_Asset("Textures/Snake/sk_body_1.png")
sk_body_img_2 = Image_Asset("Textures/Snake/sk_body_2.png")

class Snake:
    START_LENGTH = 1

    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.points = 0

        self.screen = screen;
        self.direction = input.DIR_RIGHT
        self.all_positions = []

        self.x_direction, self.y_direction = get_direction(self.direction)

    def move(self, dir):
        x_move, y_move = get_direction(dir)
        if(x_move == -self.x_direction and y_move == -self.y_direction):
            return
        
        self.direction = dir

        self.x_direction = x_move
        self.y_direction = y_move

    def update(self):
        import snake, terrain

        previous_position = {
            "x": self.x,
            "y": self.y,
            "dir": self.direction
        }
        self.all_positions.append(previous_position)

        self.x += self.x_direction
        self.y += self.y_direction

        if(self.x == snake.apple.x and self.y == snake.apple.y):
            terrain.take_apple(self)

        buffer_array = []
        length = len(self.all_positions)

        for i in range(length - self.points - Snake.START_LENGTH, length):
            buffer_array.append(self.all_positions[i])
        self.all_positions = buffer_array
    
    def render(self):
        self.render_part(self.x, self.y, self.direction, sk_head_img)
        self.render_previous()

    def render_previous(self):
        length = len(self.all_positions)
        for i in range(0, length):
            pos = self.all_positions[i]
            image = sk_tail_img if (i == 0) else sk_body_img_1

            self.render_part(pos['x'], pos['y'], pos['dir'], image)

    def render_part(self, x, y, dir, image):
        from snake import F_SIZE

        rendering_x = x * F_SIZE
        rendering_y = y * F_SIZE

        angle = get_angle(dir)
        image.render_rotated(rendering_x, rendering_y, F_SIZE, F_SIZE, angle, self.screen)

def get_direction(dir_index):
    x_move = 0
    y_move = 0
    
    if(dir_index == input.DIR_LEFT): 
        x_move = -1
    if(dir_index == input.DIR_RIGHT): 
        x_move = 1
    if(dir_index == input.DIR_UP): 
        y_move = -1
    if(dir_index == input.DIR_DOWN): 
        y_move = 1

    return (x_move, y_move)

def get_angle(dir_index):
    angle = 0

    if(dir_index == input.DIR_LEFT): 
        angle = 90
    if(dir_index == input.DIR_RIGHT): 
        angle = 270
    if(dir_index == input.DIR_UP): 
        angle = 0
    if(dir_index == input.DIR_DOWN): 
        angle = 180

    return angle