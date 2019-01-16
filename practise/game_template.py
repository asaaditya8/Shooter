import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


running = True
while running:
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	all_sprites.update()

	screen.fill(BLACK)
	all_sprites.draw(screen)
	
	pygame.display.flip()

pygame.quit()
quit()