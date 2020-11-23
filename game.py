#This try is for error catching 
try:
	import pygame
	import os
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
			["nul","nul","nul","nul","nul","nul","nul","nul","nul"],
			["nul","nul","nul","nul","nul","nul","nul","nul","nul"],
			["nul","nul","nul","nul","nul","nul","nul","nul","nul"],
			["nul","nul","nul","nul","nul","nul","nul","nul","nul"],
			["nul","nul","nul","nul","nul","nul","nul","nul","nul"]]


		def timeCounter(self):
			self.timecount = self.timecount + 1
			if self.timecount % self.FPS == 0:
				self.time = self.time + 1
				#print("Time Passed: ",self.time)

				##Print the coor of the mouse
				#print("X: " + str(self.Xmouse) + " Y: " + str(self.Ymouse))
				#self.MouseTracker()
				#self.GetBoard()

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
			self.Board[row][col] = X

		def isHoverOnBoard(self):
			x,y = pygame.mouse.get_pos()
			if(x >= 330 and x <= 977 and y>=66 and y <= 446):
				return True
			else:
				return False
		def getColRow(self):
			x,y = pygame.mouse.get_pos()
			if(x >= 330 and x <= 977 and y>=66 and y <= 446):
				row = int((x-330)/72)
				col = int((y-66)/76)
				return col,row

		def isHoverOnSeed(self):
			x,y = pygame.mouse.get_pos()
			if(x >= 20 and x <= 20+66*4 and y >= 10 and y <= 10 + 91):
				return True
			else:
				return False
		def hoverOnSeed(self):
			x,y = pygame.mouse.get_pos()
			if(x >= 20 and x <= 20+66*4 and y >= 10 and y <= 10 + 91):
				state = int((x-20)/66)+1
				return state
			
		def clearConsole(self):
			os.system("cls")
	##################### END OF LOGIC CLASS ###############

	# START OF CLASS MICE #
	class mice:
		def __init__(self):
			self.__X = 0
			self.__Y = 0
			self.state = 4 # state 0 is for null , #1 is for pea, #2 is for sun,#3 is for wal,#4 is for clear, 0 and 4 is almost the same
			self.stateInString = 'nul'
		def setState(self,x):
			self.state = x
			if self.state == 0:
				self.stateInString = 'nul'
			if self.state == 1:
				self.stateInString = 'pea'
			if self.state == 2:
				self.stateInString = 'sun'
			if self.state == 3:
				self.stateInString = 'wal'
			if self.state == 4:
				self.stateInString = 'nul'
			#print(self.state)
			#print(self.stateInString)


		def getState(self):
			return self.state

		def getStateInString(self):
			return self.stateInString
			
		def update(self):
			self.__X,self.__Y = pygame.mouse.get_pos()
			##Print the coor of the mouse
			print("X: " + str(self.__X) + " Y: " + str(self.__Y))
	#END OF CLASS MICE #

	########## P L A Y E R ##########
	class player:
		def __init__(self):
			self.name = 0
			self.sunBalance = 0
			self.score = 0
			
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print("game.py:",Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()