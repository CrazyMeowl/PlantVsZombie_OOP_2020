'''
this is the main file for the game
edit with caution 
only Push when needed
'''
'''
Board:

	5 row 
	9 column

	Xstart = 330
	Ystart = 66

	Xend = 977
	Yend = 446

	45 blocks
		size :
			width = 71
			height = 76
'''
#import the module
import pygame,sys
#start the pygame module
pygame.init()
#the size of game window
bg_width = 1000
bg_height = 500
gameWindow = pygame.display.set_mode((bg_width, bg_height))

#set caption
pygame.display.set_caption("Plant vs Zombies for O.O.P")
#control the FPS (frame)


#state of the game
gameActive = True




######## DEF GAME FUNCTION ########


###### END OF DEF GAME FUNTION ####

###### Class Define Here #####

#### Class Logic #### 
class Logic:

	def __init__(self):
		self.time = 0
		self.timecount = 0
		self.bg = pygame.image.load("Resources/bg.png")
		self.FPS = 30
		self.clock = pygame.time.Clock()
	def TimeCounter(self):
		self.timecount = self.timecount + 1
		if self.timecount % self.FPS == 0:
			self.time = self.time + 1
			print("Time Passed: ",self.time)

			##Print the coor of the mouse
			print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))

	def RedrawBG(self):
		#redraw the bg on to the window every frame
		gameWindow.blit(self.bg, (0, 0))

	def MouseTracker(self):
		##find mouse
		self.Xmouse, self.Ymouse = pygame.mouse.get_pos()
		##Print the coor of the mouse
		#print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))

###### End of Class Define ###

#### Some Variable for the game ####
game = Logic()

#### End of Variable ####
#game loop
while gameActive:
	#check event
	for event in pygame.event.get():
		##event Quit
		if event.type == pygame.QUIT:
			gameActive = False
			quit()

	#redraw game window
	game.MouseTracker()
	game.RedrawBG()
	game.TimeCounter()
	pygame.display.update()
	game.clock.tick(game.FPS)