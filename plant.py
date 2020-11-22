#This try is for error catching 
try:
	import pygame
	# START OF CLASS PLANT #
	class plant:
		List = []
		plantImgList = []
		def loadResource(ImgList):
			num = 1
			while(num <= 30):
				ImgList.append(pygame.image.load('Resources/blank.png'))
				num = num + 1
			return ImgList
		plantImgList = loadResource(plantImgList)


		def __init__(self,inRow,inCol):
			self.r = inRow
			self.c = inCol
			self.x = self.c*72 + 330
			self.y = self.r*76 + 66
			self.health = 150
			self.__frame = 0

		

		def draw(self,window):
			if self.__frame +1 == 30:
				self.__frame = 0
			else:
				self.__frame = self.__frame + 1
			window.blit(self.ImgList[self.__frame],(self.x,self.y))


	class peaShooter(plant):
		ImgList = []
		def loadResource(ImgList):
			num = 1
			while(num <= 30):
				ImgList.append(pygame.image.load('Resources/Pea/Pea'+ str(num) +'.png'))
				num = num + 1
			return ImgList
		ImgList = loadResource(ImgList)

	class sunFlower(plant):
		ImgList = []
		def loadResource(ImgList):
			num = 1
			while(num <= 30):
				ImgList.append(pygame.image.load('Resources/Sun/Sun'+ str(num) +'.png'))
				num = num + 1
			return ImgList
		ImgList = loadResource(ImgList)

	class wallNutt(plant):

		ImgList = []
		ImgList.append(pygame.image.load('Resources/Wal/Wal1.png'))
		ImgList.append(pygame.image.load('Resources/Wal/Wal2.png'))
		ImgList.append(pygame.image.load('Resources/Wal/Wal3.png'))

		def __init__(self,inRow,inCol):
			self.r = inRow
			self.c = inCol
			self.x = self.c*72 + 330
			self.y = self.r*76 + 66
			self.health = 300
			self.__frame = 0

		def draw(self,window):
			if self.health <= 300 and self.health >= 200:
				self.__frame = 0
			elif self.health < 200 and self.health >= 100:
				self.__frame = 1
			else:
				self.__frame = 2
			window.blit(self.ImgList[self.__frame],(self.x,self.y))



## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()