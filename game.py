#This try is for error catching 
try:
	import pygame
	import os
	import random
	from plant import *
	from zombie import *
	pygame.init()
	class logic:

		def __init__(self,surface):
			#for starting the window
			self.player = player(0)
			self.window	= surface
			pygame.display.set_caption("Plant vs Zombies in O.O.P")
			#for the time counter
			self.time = 0
			self.timecount = 0
			#for redraw
			self.bg = pygame.image.load("Resources/bg.png")
			#for the seed
			self.__seedX = 20
			self.__seedY = 10
			self.xPause = 20
			self.yPause = 440
			#for the game
			self.FPS = 15
			self.clock = pygame.time.Clock()

			#for MouseTracker
			self.Xmouse = 0
			self.Ymouse = 0
			#for the board
			self.board = [
			["   ","   ","   ","   ","   ","   ","   ","   ","   "],
			["   ","   ","   ","   ","   ","   ","   ","   ","   "],
			["   ","   ","   ","   ","   ","   ","   ","   ","   "],
			["   ","   ","   ","   ","   ","   ","   ","   ","   "],
			["   ","   ","   ","   ","   ","   ","   ","   ","   "]]
			self.frame = 0
			self.isActive = 'mainmenu'
			self.godmode = False
			nonsense = 1
			self.peaImgList = []
			self.sunImgList = []
			self.walImgList = []
			self.peaImg = pygame.image.load('Resources/pea.png')
			self.sunCounterImg = pygame.image.load('Resources/sunCounter.png')
			self.walImgList.append(pygame.image.load('Resources/Wal/Wal1.png'))
			self.walImgList.append(pygame.image.load('Resources/Wal/Wal2.png'))
			self.walImgList.append(pygame.image.load('Resources/Wal/Wal3.png'))
			while(nonsense <= 30):
				self.peaImgList.append(pygame.image.load('Resources/Pea/Pea'+ str(nonsense) +'.png'))
				self.sunImgList.append(pygame.image.load('Resources/Sun/Sun'+ str(nonsense) +'.png'))
				nonsense = nonsense + 2
		def godMode(self,state):
			self.godmode = state
			if(state == True):
				self.player.setSun(99999)
			else:
				self.player.setSun(0)
		def resetTheGame(self):
			self.board = [
				["   ","   ","   ","   ","   ","   ","   ","   ","   "],
				["   ","   ","   ","   ","   ","   ","   ","   ","   "],
				["   ","   ","   ","   ","   ","   ","   ","   ","   "],
				["   ","   ","   ","   ","   ","   ","   ","   ","   "],
				["   ","   ","   ","   ","   ","   ","   ","   ","   "]]
				
			self.plantList = []
			self.zomList = []
			self.peaList = []
			self.timecount = 0
			self.time = 0
			self.sunCounter = 0
			self.player.reset()
		def timeCounter(self):
			self.timecount = self.timecount + 1
			if self.timecount % self.FPS == 0:
				self.time = self.time + 1
			#print(self.time)

		def gameRedraw(self):
			#redraw the bg on to the window every frame
			self.window.blit(self.bg, (0, 0))
			self.window.blit(self.sunCounterImg,(284,10))
			self.window.blit(self.updateSunBalance(),(334,20))
			


		#update the disp
		def dispUpdate(self):
			pygame.display.update()
		#print out the board
		def getBoard(self):
			print("board state")
			print(self.board[0])
			print(self.board[1])
			print(self.board[2])
			print(self.board[3])
			print(self.board[4])
			return self.board

		def setBoard(self,inCol,inRow,mouseStateInString):
			self.board[inRow][inCol] = mouseStateInString
		def isHoverOnBoard(self):
			x,y = pygame.mouse.get_pos()
			if(x >= 330 and x <= 977 and y>=66 and y <= 446):
				return True
			else:
				return False
		def getColRow(self):
			x,y = pygame.mouse.get_pos()
			if(x >= 330 and x <= 977 and y>=66 and y <= 446):
				col = int((x-330)/72)
				row = int((y-66)/76)
				return col,row
		#seed part
		def isHoverOnSeed(self):
			x,y = pygame.mouse.get_pos()
			if(x >= self.__seedX and x <= self.__seedX+66*4 and y >= self.__seedY and y <= self.__seedY + 91):
				return True
			else:
				return False
		
		def hoverOnSeed(self):
			x,y = pygame.mouse.get_pos()
			if(x >= self.__seedX and x <= self.__seedX+66*4 and y >= self.__seedY and y <= self.__seedY + 91):
				state = int((x-20)/66)+1
				#print(state)
				return state
		## end of seed part

		#pause menu part
		def isHoverOnPause(self):
			x,y = pygame.mouse.get_pos()
			
			if(x >= self.xPause and x <= self.xPause + 50 and y>= self.yPause and y <= self.yPause + 50):
				return True
			else:
				return False

		def callPauseMenu(self):
			self.isActive = 'pausemenu'

		def callQuitMenu(self):
			self.isActive = 'quitmenu'

		def gameOver(self):
			self.isActive = 'gameover'
		##pause menu part
		def win(self):
			self.isActive = 'win'

			
		def clearConsole(self):
			os.system("cls")

		#plant list for the game (static)
		plantList = []
		peaList = []
		sunCounter = 0


		def addAPlant(self,inCol,inRow,mouseStateInString):
			
			if mouseStateInString == 'pea':
				if(self.player.subSun(100)):
					self.plantList.append(peaShooter(inCol,inRow))
					self.board[inRow][inCol] = mouseStateInString
				
			elif mouseStateInString == 'sun':
				if(self.player.subSun(50)):
					self.sunCounter = self.sunCounter + 1
					self.plantList.append(sunFlower(inCol,inRow))
					self.board[inRow][inCol] = mouseStateInString
				
			elif mouseStateInString == 'wal':
				if(self.player.subSun(50)):
					self.plantList.append(wallNutt(inCol,inRow))
					self.board[inRow][inCol] = mouseStateInString
				
		def removePlant(self,inCol,inRow):
			i = 0
			while i < len(self.plantList):
				for plant in self.plantList:
					if(plant.c == inCol and plant.r == inRow):
						#print(arraylist.index(pea))
						self.plantList.pop(self.plantList.index(plant))
						if(self.board[inRow][inCol] == 'pea'):
							self.player.addSun(100)
						elif(self.board[inRow][inCol] == 'sun'):
							self.player.addSun(50)
						elif(self.board[inRow][inCol] == 'wal'):
							self.player.addSun(50)
						self.setBoard(inCol,inRow,'   ')
				i = i + 1
		def killAPlant(self,inCol,inRow):
			i = 0
			while i < len(self.plantList):
				for plant in self.plantList:
					if(plant.c == inCol and plant.r == inRow):
						#print(arraylist.index(pea))
						self.plantList.pop(self.plantList.index(plant))
						self.setBoard(inCol,inRow,'   ')
				i = i + 1

		def checkPlantList(self):
			for plant in self.plantList:
				if(plant.health <= 0):
					self.killAPlant(plant.c,plant.r)
				plant.draw(self.window)
				if(self.timecount % 30 == 0):
					if(plant.shoot() == 1):
						#print("shot")
						self.peaList.append(pea(plant.c,plant.r))
		def checkPeaList(self):
			for pea in self.peaList:
				if(pea.x >= 1000 or pea.hit == 1):
					self.peaList.pop(self.peaList.index(pea))
				else:
					for zom in self.zomList:
						if((pea.r == zom.r) and (pea.x <= zom.x) and (pea.x + 60 >= zom.x)):
							if(self.godmode == True):
								zom.health = 0
							else:
								zom.health = zom.health - 25
							pea.hit = 1
							
					pea.move()
						#self.clearConsole()
		def drawPlant(self):
			#self.board
			if self.frame + 1 == 15:
				self.frame = 0
			else:
				self.frame = self.frame + 1
			y = 0
			x = 0
			while(y <= 4):
				x = 0
				while(x <= 8):
					if self.board[y][x] == 'pea':
						self.window.blit(self.peaImgList[self.frame],(330 + x * 72,66 + y * 76))
					if self.board[y][x] == 'sun':
						self.window.blit(self.sunImgList[self.frame],(330 + x * 72,66 + y * 76))
					x += 1
				y += 1
			for pea in self.peaList:
				self.window.blit(self.peaImg,(pea.x,pea.y))
			
			


		#######
		##ZOM##
		#######
		zomList = []
		def addAZombie(self,inCol,inRow):
			self.zomList.append(zombie(inCol,inRow))
		def checkZomList(self):
			for zom in self.zomList:
				if(zom.health <= 0):
					self.zomList.pop(self.zomList.index(zom))
		# LEVELs #
		def levelOne(self):
			i = 0
			numberOfZombie = 10
			while( i < numberOfZombie):
				A = random.randint(10,20)
				B = random.randint(0,4)
				self.addAZombie(A,B)
				i = i + 1
		def levelTwo(self):
			i = 0
			numberOfZombie = 30
			while( i < numberOfZombie):
				A = random.randint(10,20)
				B = random.randint(0,4)
				self.addAZombie(A,B)
				i = i + 1
		# Add more level Here #
		def update(self):
			levelOneStartTime = 10
			levelTwoStartTime = 70
			winTime = 110
			if(self.timecount == 15*levelOneStartTime):
				self.levelOne()
			if(self.timecount == 15*levelTwoStartTime):
				self.levelTwo()
			if(self.timecount == 15*winTime):
				self.win()
	####
		font = pygame.font.SysFont('Arial',30)
		def updateSunBalance(self):
			sunLabel = self.font.render(str(self.player.sunBalance),1,(0,0,0))
			return sunLabel

		def addSunBalance(self):
			if((self.timecount % 60 == 0)):
				self.player.sunBalance += 50
				self.player.sunBalance += 25*self.sunCounter

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
				self.stateInString = 'clr'


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
		def __init__(self,sun):
			self.name = 0
			self.sunBalance = sun
			self.score = 0

		def reset(self):
			self.name = 0
			self.sunBalance = 0
			self.score = 0
		#sun
		def addSun(self,amount):
			self.sunBalance = self.sunBalance + amount

		def subSun(self,amount):
			if(self.sunBalance - amount >= 0):
				self.sunBalance = self.sunBalance - amount
				return 1 #1 mean affordable
			else:
				return 0 #0 mean not
		def setSun(self,amount):
			self.sunBalance = amount
			

			
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print("game.py:",Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()