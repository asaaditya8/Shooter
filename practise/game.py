import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

carImg = pygame.image.load('racecar.png')

def things(x, y, w, h, c):
	pygame.draw.rect(gameDisplay, c, [x, y, w, h])

def car(x,y):
	gameDisplay.blit(carImg, (x,y))	

def message_display(text):
	largeFont = pygame.font.Font('freesansbold.ttf', 80)
	textSurface = largeFont.render(text, True, black)
	TextSurf, TextRect = textSurface, textSurface.get_rect()
	TextRect.center = (display_width/2, display_height/2)
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)

def crash():
	message_display('You crashed')
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600

x = (display_width * 0.45)
y = (display_height * 0.8)
speed = 0

thing_startx = random.randrange(0,display_width)
thing_starty = -600
thing_speed = 7
thing_w = 50
thing_h = 50

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('a bit racey')

clock = pygame.time.Clock()

crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		#print(event)
		acc = 0
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				acc -= 5
			elif event.key == pygame.K_RIGHT:
				acc += 5

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				acc=0
	'''
	friction = 0
	if acc!=0:
		speed += acc
	else: 
		if speed != 0: friction = -speed
		speed += friction
	'''
	x += acc
	gameDisplay.fill(white)
	things(thing_startx, thing_starty, thing_w, thing_h, black)
	thing_starty += thing_speed
	car(x,y)

	if x > display_width - 30 or x < 0:
		crash()
	
	if thing_starty > display_height:
		thing_starty = 0 - thing_h
		thing_startx = random.randrange(0, display_width)

	if y < thing_starty + thing_h:
		print('y crossover')
		if x> thing_startx and x< thing_startx + thing_w or x+30 > thing_startx and x+30 < thing_startx + thing_w:
			crash()

	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()