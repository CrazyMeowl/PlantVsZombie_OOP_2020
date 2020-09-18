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
bg_width = 1000
bg_height = 500
gameWindow = pygame.display.set_mode((bg_width, bg_height))
bg = pygame.image.load("Resources/bg.png")
#set caption
pygame.display.set_caption("Plant vs Zombies for O.O.P")
#control the FPS (frame)
clock = pygame.time.Clock()

#state of the game
gameActive = True




######## DEF GAME FUNCTION ########
def RedrawBG():
	#redraw the bg on to the window every frame
	gameWindow.blit(bg, (0, 0))

def MouseTracker():
	##find mouse
	Xmouse , Ymouse = pygame.mouse.get_pos()
	##Print the coor of the mouse
	print("X: " + str(Xmouse) + " Y: " + str(Ymouse))

###### END OF DEF GAME FUNTION ####
#game loop
while gameActive:
	#check event
	for event in pygame.event.get():
		##event Quit
		if event.type == pygame.QUIT:
			gameActive = False
			quit()

	#redraw game window
	MouseTracker()
	RedrawBG()
	pygame.display.update()
	FPS = 30
	clock.tick()