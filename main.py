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
	
	#menubutton = button((0,255,0), 150,255,250,100,'Menu')
	game = logic(surface)
	mainMenu = mainmenu()
	pauseMenu = pausemenu()
	gameOver = gameover()
	quitMenu = quitmenu()

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
	
	while True:
		while isActive == 'mainmenu':
			mainMenu.menu.mainloop(surface)
			game.resetTheGame()
			if(mainMenu.menu.enable() == None):
				isActive = 'game'

		while isActive == 'pausemenu':
			pauseMenu.menu.mainloop(surface)
			if(pauseMenu.menu.enable() == None and pauseMenu.state == 'resume'):
				isActive = 'game'
			else:
				isActive = 'mainmenu'
		
		while isActive == 'gameover':
			gameOver.menu.mainloop(surface)
			if(gameOver.menu.enable() == None and gameOver.state == 'restart'):
				game.resetTheGame()
				isActive = 'game'
			else:
				isActive = 'mainmenu'				

		while isActive == 'quitmenu':
			quitMenu.menu.mainloop(surface)
			if(quitMenu.menu.enable() == None and quitMenu.state == 'resume'):
				isActive = 'game'
			

		#game loop
		while isActive == 'game':
			#check event
			if(game.timecount == 150):
				game.levelOne()
			for event in pygame.event.get():
				#Mouse.update()
				##event Quit
				if event.type == pygame.QUIT:
					isActive = 'quitmenu'
					#quit()
				
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if(game.isHoverOnBoard()):
						#print(game.getColRow())
						xd,yd = game.getColRow()
					if(game.isHoverOnSeed()):
						Mouse.setState(game.hoverOnSeed())
					if(game.isHoverOnPause()):
						isActive = game.callPauseMenu()
						
						
						
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
									#game.getBoard()
								
								
			
			game.addSunBalance()
			game.gameRedraw()
			
			
			game.checkPlantList()
			game.checkPeaList()
			game.checkZomList()
			#print(game.plantList)
			for zom in game.zomList:
				if(zom.stop == 0):
					if(zom.move() == 0):
							isActive = game.gameOver()

				zom.isCollide(game.plantList)
				#print(game.plantList)
				#print(zom.stop)
				zom.draw(game.window)

			game.drawPlant()
			game.dispUpdate() 
			game.timeCounter()
			game.clock.tick(game.FPS)

		
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print("main.py",Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()