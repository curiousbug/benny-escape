import pygame

WIDTH = 800
HEIGHT = 600
box_x = 50
box_y = 150
hand_y = 320

WHITE = 200, 200, 200

def draw():
    screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    screen.clear()
    screen.fill(WHITE)
    screen.blit(images.hoopa, (50, 150))
    screen.blit(images.hoopac, (400, 150))

    box = Rect((box_x, box_y), (700, 300))
    screen.draw.filled_rect(box, WHITE)

    if hand_y > 10:
    	screen.blit(images.pen, (230, hand_y))
    	screen.blit(images.pen2, (670, hand_y))

def game_loop():
	global box_x, box_y, hand_y
	box_y -= 1
	hand_y -= 1

clock.schedule_interval(game_loop, 0.05)
