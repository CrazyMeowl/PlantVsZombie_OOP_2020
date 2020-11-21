#This try is for error catching 
try:
	import pygame
	class logic:

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
			self.__seedX = 20
			self.__seedY = 10
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


		def timeCounter(self):
			self.timecount = self.timecount + 1
			if self.timecount % self.FPS == 0:
				self.time = self.time + 1
				#print("Time Passed: ",self.time)

				##Print the coor of the mouse
				#print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))
				#self.MouseTracker()
				#self.GetBoard()

		def mouseTracker(self):
			##find mouse
			self.Xmouse, self.Ymouse = pygame.mouse.get_pos()
			##Print the coor of the mouse
			print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))
			return self.Xmouse, self.Ymouse

		def boardCheck(self,inX,inY):
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
			self.window.blit(self.PEASEED,(self.__seedX,self.__seedY))
			self.window.blit(self.SUNSEED,(self.__seedX + 66,self.__seedY))
			self.window.blit(self.WALSEED,(self.__seedX + 66 * 2,self.__seedY))
			self.window.blit(self.SHOVEL,(self.__seedX + 66 * 3,self.__seedY))

		def menuRedraw(self):
			pass


		#update the disp
		def dispUpdate(self):
			pygame.display.update()
		#print out the board
		def getBoard(self):
			print("Board state")
			print(self.Board[0])
			print(self.Board[1])
			print(self.Board[2])
			print(self.Board[3])
			print(self.Board[4])
			return self.Board
		def setBoard(self,row,col,X):
			if row != 0 and col != 0:
				self.Board[row - 1][col - 1] = X
	##################### END OF LOGIC CLASS ###############

	# START OF CLASS MICE #
	class mice:
		def __init__(self):
			self.__X = 0
			self.__Y = 0
			self.__state = "none"
		
		def setState(self,X):
			self.__state = str(X)
			#print(self.state)

		def getState(self):
			print(self.__state)
			if self.__state == "Pea":
				return 1
			elif self.__state == "Sun":
				return 2
			elif self.__state == "Wall":
				return 3
			elif self.__state == "Clear":
				return 0
			
		def update(self):
			self.__X,self.__Y = pygame.mouse.get_pos()
			##Print the coor of the mouse
			print("X: " + str(self.__X) + " Y: " + str(self.__Y))
	#END OF CLASS MICE #

			
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()