#This try is for error catching 
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
	import os
	import pygame,sys
	pygame.init()
	#state of the game
	gameActive = True
	menuActive = False



	###### Class Define Here #####

	##### Button
	class button():
		def __init__(self, color, x,y,width,height, text=''):
			self.color = color
			self.x = x
			self.y = y
			self.width = width
			self.height = height
			self.text = text

		def draw(self,win,outline=None):
			#Call this method to draw the button on the screen
			if outline:
				pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
				
			pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
			
			if self.text != '':
				font = pygame.font.SysFont('comicsans', 60)
				text = font.render(self.text, 1, (0,0,0))
				win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

		def isOver(self, pos):
			#Pos is the mouse position or a tuple of (x,y) coordinates
			if pos[0] > self.x and pos[0] < self.x + self.width:
				if pos[1] > self.y and pos[1] < self.y + self.height:
					return True
				
			return False
	#####

	#### Class Logic #### 
	class Logic:

		def __init__(self):
			#for starting the window
			self.__bg_width = 1000
			self.__bg_height = 500
			self.window	= pygame.display.set_mode((self.__bg_width, self.__bg_height))
			pygame.display.set_caption("Plant vs Zombies in O.O.P")
			#for the time counter
			self.time = 0
			self.timecount = 0
			#for redraw
			self.bg = pygame.image.load("Resources/bg.png")
				#for the seed
			self.seedX = 20
			self.seedY = 10
			self.PEASEED = pygame.image.load("Resources/SeedPea.png")
			self.SUNSEED = pygame.image.load("Resources/SeedSun.png")
			self.WALSEED = pygame.image.load("Resources/SeedWal.png")
			self.SHOVEL = pygame.image.load("Resources/Shovel.png")
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
			print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))
			return self.Xmouse, self.Ymouse

		def BoardCheck(self,inX,inY):
			self.Row = int(((inY - 67)/76)+1)
			self.YBoard = ((self.Row - 1) * 76) + 67
			self.Col = int(((inX - 330)/71)+1)
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

		def gameRedraw(self):
			#redraw the bg on to the window every frame
			self.window.blit(self.bg, (0, 0))
			self.window.blit(self.PEASEED,(self.seedX,self.seedY))
			self.window.blit(self.SUNSEED,(self.seedX + 66,self.seedY))
			self.window.blit(self.WALSEED,(self.seedX + 66 * 2,self.seedY))
			self.window.blit(self.SHOVEL,(self.seedX + 66 * 3,self.seedY))

		def menuRedraw(self):
			pass


		#update the disp
		def dispUpdate(self):
			pygame.display.update()
		#print out the board
		def GetBoard(self):
			print("Board state")
			print(self.Board[0])
			print(self.Board[1])
			print(self.Board[2])
			print(self.Board[3])
			print(self.Board[4])
			return self.Board
		def SetBoard(self,row,col,X):
			if row != 0 and col != 0:
				self.Board[row - 1][col - 1] = X
	##################### END OF LOGIC CLASS ###############

	# START OF CLASS MICE #
	class Mice:
		def __init__(self):
			self.__X = 0
			self.__Y = 0
			self.__state = "none"
		
		def SetState(self,X):
			self.__state = str(X)
			#print(self.state)

		def GetState(self):
			print(self.__state)
			if self.__state == "Pea":
				return 1
			elif self.__state == "Sun":
				return 2
			elif self.__state == "Wall":
				return 3
			elif self.__state == "Clear":
				return 0
			
		def Update(self):
			self.__X,self.__Y = pygame.mouse.get_pos()
			##Print the coor of the mouse
			print("X: " + str(self.__X) + " Y: " + str(self.__Y))
	#END OF CLASS MICE #

	# START OF CLASS PLANT #
	class PeaShooter:
		List = []
		Imglist = []
		num = 1
		while(num <= 30):
			Imglist.append(pygame.image.load('Resources/Pea/Pea'+ str(num) +'.png'))
			num = num + 1

		def __init__(self,inRow,inCol):
			self.R = inRow
			self.C = inCol
			self.X = 0
			self.Y = 0
			self.Health = 150
			self.Frame = 0

		def Draw(self,window):
			if self.Frame +1 >= 30:
				self.Frame = 0
			else:
				self.Frame = self.Frame + 1
			window.blit(self.Imglist[self.Frame],(self.X,self.Y))


	class SunFlower:
		List = []
		Imglist = []
		num = 1
		while(num <= 30):
			Imglist.append(pygame.image.load('Resources/Sun/Sun'+ str(num) +'.png'))
			num = num + 1

		def __init__(self,inRow,inCol):
			self.R = inRow
			self.C = inCol
			self.X = 0
			self.Y = 0
			self.Health = 150
			self.Frame = 0

		def Draw(self,window):
			if self.Frame +1 >= 30:
				self.Frame = 0
			else:
				self.Frame = self.Frame + 1
			window.blit(self.Imglist[self.Frame],(self.X,self.Y))
	# END OF CLASS PLANT #




	###### End of Class Define ###

	#### Some Variable for the game ####
	P1 = PeaShooter(2,2)
	#menubutton = button((0,255,0), 150,255,250,100,'Menu')
	game = Logic()
	Mouse = Mice()
	RowDown = 0
	RowUp = 0
	ColDown = 0
	ColUp = 0
	Mouse.SetState("Pea")
	#### End of Variable ####


	#### C L E A R   S C R E E N ####
	run = os.system("cls")
	#################################
	#game loop
	while gameActive:
		#check event
		for event in pygame.event.get():
			##event Quit
			if event.type == pygame.QUIT:
				gameActive = False
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				X1,Y1 = game.MouseTracker()
				RowDown, ColDown = game.BoardCheck(X1,Y1)
			if event.type == pygame.MOUSEBUTTONUP:
				X2,Y2 = game.MouseTracker()
				RowUp, ColUp = game.BoardCheck(X2,Y2)
				if RowDown == RowUp and ColDown == ColUp:
					run = os.system("cls")
					game.SetBoard(RowDown,ColDown,Mouse.GetState())
					game.GetBoard()
					
		#redraw game window

		# game.MouseTracker()
		# Mouse.Update() #print the current position of the mouse constanly
		if(gameActive == 1):
			game.gameRedraw()
			#menubutton.draw(game.window,(0,0,0))
			P1.Draw(game.window)
		else:
			game.menuRedraw()

		game.dispUpdate() 

		game.TimeCounter()
		game.clock.tick(game.FPS)
		
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()