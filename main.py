'''
this is the main file for the game
edit with caution 
only Push when needed
'''

#import the module
import pygame,sys
#start the pygame module
pygame.init()
#the size of game window
bg_width = 500
bg_height = 500
gameWindow = pygame.display.set_mode((bg_width, bg_height))
#set caption
pygame.display.set_caption("Plant vs Zombies for O.O.P")
#control the FPS (frame)
clock = pygame.time.Clock()

#state of the game
gameActive = True

#game loop
while gameActive:
	#check event
	for event in pygame.event.get():
		##event Quit
		if event.type == pygame.QUIT:
			gameActive = False
			quit()
	#redraw game window
	pygame.display.update()
	FPS = 30
	clock.tick()