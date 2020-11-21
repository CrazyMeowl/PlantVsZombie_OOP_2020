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
	from game import *
	from plant import *
	pygame.init()
	#state of the game
	gameActive = True
	menuActive = False



	###### Class Define Here #####

	

	#### Some Variable for the game ####
	P1 = peaShooter(2,2)
	#menubutton = button((0,255,0), 150,255,250,100,'Menu')
	game = logic()
	Mouse = mice()
	RowDown = 0
	RowUp = 0
	ColDown = 0
	ColUp = 0
	Mouse.setState("Pea")
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
				pass
			if event.type == pygame.MOUSEBUTTONUP:
				pass
				
		#redraw game window

		# game.MouseTracker()
		# Mouse.Update() #print the current position of the mouse constanly
		if(gameActive == 1):
			game.gameRedraw()
			#menubutton.draw(game.window,(0,0,0))
			P1.draw(game.window)
		else:
			game.menuRedraw()

		game.dispUpdate() 

		game.timeCounter()
		game.clock.tick(game.FPS)
		
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()