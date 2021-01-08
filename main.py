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
	from pygame import mixer
	from game import *
	from plant import *
	from zombie import *
	from menu import *
	#from mainmenu import *

	pygame.init()
	surface = pygame.display.set_mode((1000, 500))

	#### Some Variable for the game ####
	
	#menubutton = button((0,255,0), 150,255,250,100,'Menu')
	game = logic(surface,mixer)
	mainMenu = mainmenu()
	pauseMenu = pausemenu()
	gameOver = gameover()
	quitMenu = quitmenu()
	winMenu = winmenu()

	Mouse = mice()

	RowDown = 0
	RowUp = 0
	ColDown = 0
	ColUp = 0
	Mouse.setState(1)
	level = 0
	a = pea(1,1)
	#### End of Variable ####


	#### C L E A R   S C R E E N ####
	game.clearConsole()
	#################################
	game.backgroundMusic()
	while True:
		
		while game.isActive == 'mainmenu':
			mainMenu.menu.mainloop(surface)
			mainMenu.menu.enable()
			game.resetTheGame()
			game.godMode(False)
			game.isActive = 'game'

				

		while game.isActive == 'pausemenu':
			pauseMenu.menu.mainloop(surface)
			pauseMenu.menu.enable()
			
			if(pauseMenu.state == 'resume'):
				game.isActive = 'game'
				game.unpauseBackgroundMusic()
			else:
				game.isActive = 'mainmenu'
				game.unpauseBackgroundMusic()
			
		
		while game.isActive == 'gameover':
			gameOver.menu.mainloop(surface)
			gameOver.menu.enable()
			if(gameOver.state == 'restart'):
				game.resetTheGame()
				game.godMode(False)
				game.isActive = 'game'
				game.unpauseBackgroundMusic()
			elif(gameOver.state == 'godmode'):
				game.resetTheGame()
				game.godMode(True)
				game.isActive = 'game'
				game.unpauseBackgroundMusic()
			else:
				game.isActive = 'mainmenu'
				game.unpauseBackgroundMusic()	

		while game.isActive == 'win':
			winMenu.menu.mainloop(surface)
			winMenu.menu.enable()
			if(winMenu.state == 'restart'):
				game.resetTheGame()
				game.godMode(False)
				game.isActive = 'game'
				game.unpauseBackgroundMusic()
			elif(winMenu .state == 'godmode'):
				game.resetTheGame()
				game.godMode(True)
				game.isActive = 'game'
				game.unpauseBackgroundMusic()
			else:
				game.isActive = 'mainmenu'
				game.unpauseBackgroundMusic()		

		while game.isActive == 'quitmenu':
			quitMenu.menu.mainloop(surface)
			if(quitMenu.menu.enable() == None and quitMenu.state == 'resume'):
				game.isActive = 'game'
				game.unpauseBackgroundMusic()

			
		
			
		#game loop

		
		while game.isActive == 'game':
			#for background music:
			
			
			for event in pygame.event.get():
				#Mouse.update()
				##event Quit
				if event.type == pygame.QUIT:
					game.callQuitMenu()
					#quit()
				
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if(game.isHoverOnBoard()):
						#print(game.getColRow())
						xd,yd = game.getColRow()
					if(game.isHoverOnSeed()):
						Mouse.setState(game.hoverOnSeed())
					if(game.isHoverOnPause()):
						
						game.callPauseMenu()
						
						
						
				elif event.type == pygame.MOUSEBUTTONUP:
					if(game.isHoverOnBoard()):
						#print(game.getColRow())
						xu,yu = game.getColRow()
						#print(xu,yu)
						if(xu == xd and yu == yd):
							if(Mouse.getStateInString() == 'clr'):
								game.removePlant(xd,yd)
							else:
								if(game.board[yd][xd] == '   '):
									#game.setBoard(xd,yd,Mouse.getStateInString())
									game.addAPlant(xd,yd,Mouse.getStateInString())
									game.clearConsole()
									game.getBoard()
								
								
			
			game.mainUpdate()

		
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print("main.py",Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()