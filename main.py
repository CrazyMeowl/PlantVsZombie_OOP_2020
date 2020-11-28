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
	import pygame_menu
	import pygame,sys
	from game import *
	from plant import *
	from zombie import *
	from menu import *
	#from mainmenu import *

	pygame.init()
	surface = pygame.display.set_mode((1000, 500))
	#state of the game
	isActive = 'mainmenu'
	PAUSE = False





	#### Some Variable for the game ####
	P1 = peaShooter(3,2)
	P2 = sunFlower(2,2)
	P3 = wallNutt(4,2)
	Z1 = zombie(4,8)
	#menubutton = button((0,255,0), 150,255,250,100,'Menu')
	game = logic(surface)
	mainMenu = mainmenu()
	pauseMenu = pausemenu()

	Mouse = mice()

	RowDown = 0
	RowUp = 0
	ColDown = 0
	ColUp = 0
	Mouse.setState(1)
	#### End of Variable ####


	#### C L E A R   S C R E E N ####
	game.clearConsole()
	#################################
	while True:
		while isActive == 'mainmenu':
			mainMenu.menu.mainloop(surface)
			if(mainMenu.menu.enable() == None):
				isActive = 'game'

		while isActive == 'pausemenu':
			pauseMenu.menu.mainloop(surface)
			if(pauseMenu.menu.enable() == None and pauseMenu.state == 'normal'):
				isActive = 'game'
			else:
				isActive = 'mainmenu'
			
		#game loop
		while isActive == 'game':
			#check event
			for event in pygame.event.get():
				##event Quit
				if event.type == pygame.QUIT:
					isActive = 'menu'
					quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if(game.isHoverOnBoard()):
						#print(game.getColRow())
						xd,yd = game.getColRow()
					if(game.isHoverOnSeed()):
						Mouse.setState(game.hoverOnSeed())
					if(game.isHoverOnPause()):
						isActive = game.callPauseMenu(isActive)
						
						
						
				if event.type == pygame.MOUSEBUTTONUP:
					if(game.isHoverOnBoard()):
						#print(game.getColRow())
						xu,yu = game.getColRow()
						print(xu,yu)
						if(xu == xd and yu == yd):
							if(Mouse.getStateInString() == 'clr'):
								game.setBoard(xd,yd,'   ')
								game.removePlant(xd,yd)
							else:
								if(game.board[yd][xd] == '   '):
									game.setBoard(xd,yd,Mouse.getStateInString())
									game.addAPlant(xd,yd,Mouse.getStateInString())
								
								
									
					game.clearConsole()
					game.getBoard()
				
				game.gameRedraw()
				#menubutton.draw(game.window,(0,0,0))
				for plant in game.plantList:
					plant.draw(game.window)
				Z1.move()
				Z1.draw(game.window)
				P3.health = P3.health - 5
			

			game.dispUpdate() 
			game.timeCounter()
			game.clock.tick(game.FPS)

		
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print("main.py",Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()