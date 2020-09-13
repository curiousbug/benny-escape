WIDTH = 800
HEIGHT = 600
box_x = 200
box_y = 180

BLACK = 0, 0, 0

def draw():
    screen.clear()
    screen.blit(images.phione, (200, 150))

    box = Rect((box_x, box_y), (320, 250))
    screen.draw.filled_rect(box, BLACK)

def game_loop():
    global box_x, box_y
    box_y -= 1

clock.schedule_interval(game_loop, 0.05)
