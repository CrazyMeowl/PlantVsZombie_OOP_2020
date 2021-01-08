#This try is for error catching

#PEA DELAY 3 SEC#
#SUN DELAY 15 SEC#
try:
	import pygame
	# START OF CLASS PLANT #
	class pea:
		pass
	class plant:
		List = []
		plantImgList = []


		def __init__(self,inCol,inRow):
			self.r = inRow
			self.c = inCol
			self.x = self.c*72 + 330
			self.y = self.r*76 + 66
			self.health = 150
			self.__frame = 0

			self.rightBorder = self.x + 36

		def shoot(self):
			#print("Shooting")
			return 0
#this draw method is not useless
#it for WalNut #DoNotRemove Thingy

	class peaShooter(plant):
		ImgList = []
		def loadResource(ImgList):
			num = 1
			while(num <= 30):
				ImgList.append(pygame.image.load('Resources/Pea/Pea'+ str(num) +'.png'))
				num = num + 2
			return ImgList
		ImgList = loadResource(ImgList)

		def shoot(self):
			return 1
###################################################################################################################
		


	class sunFlower(plant):
		ImgList = []
		def loadResource(ImgList):
			num = 1
			while(num <= 30):
				ImgList.append(pygame.image.load('Resources/Sun/Sun'+ str(num) +'.png'))
				num = num + 2
			return ImgList
		ImgList = loadResource(ImgList)

	class wallNutt(plant):

		ImgList = []
		ImgList.append(pygame.image.load('Resources/Wal/Wal1.png'))
		ImgList.append(pygame.image.load('Resources/Wal/Wal2.png'))
		ImgList.append(pygame.image.load('Resources/Wal/Wal3.png'))

		def __init__(self,inCol,inRow):
			self.r = inRow
			self.c = inCol
			self.x = self.c*72 + 330
			self.y = self.r*76 + 66
			self.health = 300
			self.__frame = 0
			self.rightBorder = self.x + 36

		

	class pea():
		def __init__(self,inCol,inRow):
			self.r = inRow
			self.c = inCol
			self.x = self.c*72 + 330
			self.y = self.r*76 + 66
			self.hit = 0
			#print("pea")
			
		def move(self):
			if(self.x <= 1000):
				self.x = self.x + 5
			#print("X: " + str(self.x) + " Y: " + str(self.y))

## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()