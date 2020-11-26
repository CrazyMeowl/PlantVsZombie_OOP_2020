#This try is for error catching 
try:
	import pygame
	import os
	import pygame_menu


	


	

	class mainmenu:
		def start(self):
			 self.menu.disable()
		def quit(self):
			quit()
		def __init__(self):
			self.theme = pygame_menu.themes.THEME_ORANGE.copy()
			self.theme.title_background_color=(0, 0, 0)
			self.theme.background_color=(0, 10, 0, 25)
			self.font = pygame_menu.font.FONT_NEVIS
			self.theme.widget_font = self.font
			self.image = pygame_menu.baseimage.BaseImage(image_path='Resources/bgmenu.png', drawing_mode=pygame_menu.baseimage.IMAGE_MODE_SIMPLE)
			self.theme.background_color = self.image
			self.theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

			self.menu = pygame_menu.Menu(500, 1000, ' ',theme = self.theme)
			self.menu.add_button('P L A Y', self.start)
			self.menu.add_button('Quit',self.quit)

	class pausemenu(mainmenu):

		def resume(self):
			self.state = 'normal'
			self.menu.disable()

		def callMain(self):
			self.state = 'mainmenu'
			self.menu.disable()

		def quit(self):
			quit()

		def __init__(self):
			self.theme = pygame_menu.themes.THEME_ORANGE.copy()
			self.theme.title_background_color=(0, 0, 0)
			self.theme.background_color=(0, 10, 0, 25)
			self.font = pygame_menu.font.FONT_NEVIS
			self.theme.widget_font = self.font
			self.image = pygame_menu.baseimage.BaseImage(image_path='Resources/bgmenu.png', drawing_mode=pygame_menu.baseimage.IMAGE_MODE_SIMPLE)
			self.theme.background_color = self.image
			self.theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
			self.state = 'normal'
			self.menu = pygame_menu.Menu(500, 1000, ' ',theme = self.theme)
			self.menu.add_button('Resume the game', self.resume)
			self.menu.add_button('Return to main menu', self.callMain)
			self.menu.add_button('Quit',self.quit)


		


		
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()