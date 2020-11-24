#This try is for error catching 
try:
	import pygame
	import os
	import pygame_menu

	pygame.init()
	surface = pygame.display.set_mode((1000, 500))


	def continue_the_game():
		pass

	def return_the_menu():
		menu = os.system("python mainmenu.py")
		print(menu)

	def quit_the_game():
		pass



	mytheme = pygame_menu.themes.THEME_ORANGE.copy()
	mytheme.title_background_color=(0, 0, 0)
	mytheme.background_color=(0, 10, 0, 25)
	font = pygame_menu.font.FONT_8BIT
	mytheme.widget_font = font
	myimage = pygame_menu.baseimage.BaseImage(image_path='Resources/bgpause.jpg', drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER)
	mytheme.background_color = myimage
	mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
	menu = pygame_menu.Menu(500, 1000, 'PAUSE MENU',theme = mytheme)
	menu.add_button('Continue', continue_the_game)
	menu.add_button('Return the menu', return_the_menu)
	menu.add_button(' Quit?', pygame_menu.events.EXIT)

	menu.mainloop(surface)
			
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()
