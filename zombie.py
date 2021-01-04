#This try is for error catching 
try:
	import pygame
	# START OF CLASS PLANT #
	class zombie:
		List = []
		ImgList = []
		def loadResource(ImgList):
			num = 1
			while(num <= 12):
				ImgList.append(pygame.image.load('Resources/Zom/Zom'+ str(num) +'.png'))
				num = num + 1
			return ImgList
		ImgList = loadResource(ImgList)


		def __init__(self,inCol,inRow):
			self.r = inRow
			self.c = inCol
			self.x = self.c*72 + 330
			self.y = self.r*76 + 66
			self.health = 150
			self.__frame = 0
			self.stop = 0
			#self.time = inTime

		

		def draw(self,window):
			if self.__frame +1 == 12:
				self.__frame = 0
			else:
				self.__frame = self.__frame + 1
			window.blit(self.ImgList[self.__frame],(self.x,self.y))
		def move(self):
			if self.x >= 330:
				self.x = self.x - 1
				return 1
			else:
				#print("Game Over")
				return 0
		
		def attack(self,inPlant):
			inPlant.health = inPlant.health - 2.5
			if(inPlant.health <= 0):
				self.stop = 0
				
		def isCollide(self,inPlant):
			if(self.x == inPlant.rightBorder and self.r == inPlant.r):
				self.stop = 1
				self.attack(inPlant)
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()