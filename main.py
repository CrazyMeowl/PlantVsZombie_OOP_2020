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
			#for starting the window
			self.bg_width = 1000
			self.bg_height = 500
			self.window	= pygame.display.set_mode((self.bg_width, self.bg_height))
			pygame.display.set_caption("Plant vs Zombies for O.O.P")
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
				print("Time Passed: ",self.time)

				##Print the coor of the mouse
				#print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))
				#self.MouseTracker()
				self.GetBoard()

		def MouseTracker(self):
			##find mouse
			self.Xmouse, self.Ymouse = pygame.mouse.get_pos()
			##Print the coor of the mouse
			#print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))
			return self.Xmouse, self.Ymouse
		def BoardCheck(self):
			if self.Ymouse > 66 and self.Ymouse < 143:
				self.YBoard = 67
				self.Row = 1  
			elif self.Ymouse < 219:
				self.YBoard = 143
				self.Row = 2
			elif self.Ymouse < 295:
				self.YBoard = 219
				self.Row = 3
			elif self.Ymouse < 371:
				self.YBoard = 295
				self.Row = 4
			elif self.Ymouse < 447:
				self.YBoard = 371
				self.Row = 5
			
			if self.Xmouse > 329 and self.Xmouse < 402 :
				self.XBoard = 330
				self.Col = 1
			elif self.Xmouse < 474 :
				self.XBoard = 402
				self.Col = 2
			elif self.Xmouse < 546 :
				self.XBoard = 474
				self.Col = 3
			elif self.Xmouse < 618 :
				self.XBoard = 546 
				self.Col = 4
			elif self.Xmouse < 690 :
				self.XBoard = 618
				self.Col = 5
			elif self.Xmouse < 762 :
				self.XBoard = 690
				self.Col = 6
			elif self.Xmouse < 834 :
				self.XBoard = 762
				self.Col = 7
			elif self.Xmouse < 906 :
				self.XBoard = 834
				self.Col = 8
			elif self.Xmouse < 978 :
				self.XBoard = 906
				self.Col = 9

			if self.Ymouse < 66 or self.Ymouse > 447 or self.Xmouse < 330 or self.Xmouse > 977:
				self.XBoard = 1001
				self.YBoard = 5001
				self.Row = 0
				self.Col = 0
			return self.Row,self.Col
		def RedrawBG(self):
			#redraw the bg on to the window every frame
			self.window.blit(self.bg, (0, 0))
			pygame.display.update()
		def GetBoard(self):
			print(self.Board[0])
			print(self.Board[1])
			print(self.Board[2])
			print(self.Board[3])
			print(self.Board[4])
		def SetBoard(self,row,col,X):
			if row != 0 and col != 0:
				self.Board[row - 1][col - 1] = X

			
	###### End of Class Define ###

	#### Some Variable for the game ####
	game = Logic()
	RowDown = 0
	RowUp = 0
	ColDown = 0
	ColUp = 0
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
					game.SetBoard(RowDown,ColDown,1)
					#game.GetBoard()
		#redraw game window
		#game.MouseTracker()
		game.RedrawBG()
		game.TimeCounter()
		game.clock.tick(game.FPS)
		

except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()