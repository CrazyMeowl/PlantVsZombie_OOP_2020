try:
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
				width = 72
				height = 76
	'''
	#import the module
	import pygame,sys
	pygame.init()
	#state of the game
	gameActive = True
	menuActive = False



	###### Class Define Here #####
	#### Class Logic #### 
	class Logic:

		def __init__(self):
			#for starting the window
			self.bg_width = 1000
			self.bg_height = 500
			self.window	= pygame.display.set_mode((self.bg_width, self.bg_height))
			pygame.display.set_caption("Plant vs Zombies in O.O.P")
			#for the time counter
			self.time = 0
			self.timecount = 0
			#for redraw
			self.bg = pygame.image.load("Resources/bg.png")
			self.FPS = 30
			self.clock = pygame.time.Clock()
			#for MouseTracker
			self.Xmouse = 0
			self.Ymouse = 0
			#for the board
			self.Board = [
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0]]


		def TimeCounter(self):
			self.timecount = self.timecount + 1
			if self.timecount % self.FPS == 0:
				self.time = self.time + 1
				#print("Time Passed: ",self.time)

				##Print the coor of the mouse
				#print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))
				#self.MouseTracker()
				#self.GetBoard()

		def MouseTracker(self):
			##find mouse
			self.Xmouse, self.Ymouse = pygame.mouse.get_pos()
			##Print the coor of the mouse
			#print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))
			return self.Xmouse, self.Ymouse
		def BoardCheck(self):
			self.Row = int(((self.Ymouse - 67)/76)+1)
			self.YBoard = ((self.Row - 1) * 76) + 67
			self.Col = int(((self.Xmouse - 330)/71)+1)
			self.XBoard = ((self.Col - 1) * 72) + 330
			if self.Row <= 0 or self.Row > 5 or self.Col <= 0 or self.Col > 9:
				self.XBoard = 1001
				self.YBoard = 501
				self.Row = 0
				self.Col = 0
			'''
			print("XBoard: ",self.XBoard)
			print("YBoard: ",self.YBoard)
			print("Row: ",self.Row)
			print("Col: ",self.Col)
			'''
			return self.Row,self.Col

		def RedrawBG(self):
			#redraw the bg on to the window every frame
			self.window.blit(self.bg, (0, 0))
			pygame.display.update()
		def GetBoard(self):
			print("Board state")
			print(self.Board[0])
			print(self.Board[1])
			print(self.Board[2])
			print(self.Board[3])
			print(self.Board[4])
		def SetBoard(self,row,col,X):
			if row != 0 and col != 0:
				self.Board[row - 1][col - 1] = X
	##################### END OF LOGIC CLASS ###############
	# START OF CLASS MICE #
	class Mice:
		def __init__(self):
			self.X = 0
			self.Y = 0
			self.state = "none"
	
		def SetState(self,X):
			self.state = str(X)
			print(self.state)

		def getState(self):
			return self.state
	#END OF CLASS MICE #

	# START OF CLASS PLANT #

	# END OF CLASS PLANT #




	###### End of Class Define ###

	#### Some Variable for the game ####
	game = Logic()
	Mouse = Mice()
	RowDown = 0
	RowUp = 0
	ColDown = 0
	ColUp = 0
	Mouse.SetState("Pea")
	#### End of Variable ####
	#game loop
	while gameActive:
		#check event
		for event in pygame.event.get():
			##event Quit
			if event.type == pygame.QUIT:
				gameActive = False
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				game.MouseTracker()
				RowDown, ColDown = game.BoardCheck()
			if event.type == pygame.MOUSEBUTTONUP:
				game.MouseTracker()
				RowUp, ColUp = game.BoardCheck()
				if RowDown == RowUp and ColDown == ColUp:
					if Mouse.state == "Pea":
						game.SetBoard(RowDown,ColDown,1)
					elif Mouse.state ==  "Sun":
						game.SetBoard(RowDown,ColDown,2)
					elif Mouse.state ==  "Wall":
						game.SetBoard(RowDown,ColDown,3)
					elif Mouse.state == "Clear":
						game.SetBoard(RowDown,ColDown,0)
					game.GetBoard()
					
		#redraw game window
		game.MouseTracker()
		game.RedrawBG()
		game.TimeCounter()
		game.clock.tick(game.FPS)
		

except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()