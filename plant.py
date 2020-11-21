#This try is for error catching 
try:
	import pygame
	# START OF CLASS PLANT #
	class plant:
		List = []
		Imglist = []
		num = 1
		while(num <= 30):
			Imglist.append(pygame.image.load('Resources/blank.png'))
			num = num + 1



		def __init__(self,inRow,inCol):
			self.R = inRow
			self.C = inCol
			self.X = 0
			self.Y = 0
			self.Health = 150
			self.Frame = 0

		

		def draw(self,window):
			if self.Frame +1 >= 30:
				self.Frame = 0
			else:
				self.Frame = self.Frame + 1
			window.blit(self.Imglist[self.Frame],(self.X,self.Y))
	# END OF CLASS PLANT #
	# inheritance
	class peaShooter(plant):
		Imglist = []
		num = 1
		while(num <= 30):
			Imglist.append(pygame.image.load('Resources/Pea/Pea'+ str(num) +'.png'))
			num = num + 1



## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()