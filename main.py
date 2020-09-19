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
pygame.init()
#state of the game
gameActive = True
###### Class Define Here #####
#### Class Logic #### 
class Logic:

	def __init__(self):
		self.bg_width = 1000
		self.bg_height = 500
		self.window	= pygame.display.set_mode((self.bg_width, self.bg_height))
		pygame.display.set_caption("Plant vs Zombies for O.O.P")
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

	def MouseTracker(self):1
		##find mouse
		self.Xmouse, self.Ymouse = pygame.mouse.get_pos()
		##Print the coor of the mouse
		#print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))

	def RedrawBG(self):
		#redraw the bg on to the window every frame
		self.window.blit(self.bg, (0, 0))
		pygame.display.update()
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
	game.clock.tick(game.FPS)