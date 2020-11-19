import pygame as pg
from menu import MainMenu
class Game():
	def __init__(self):
		pg.init()
		self.running , self.playing = True, False
		self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False
		self.DISPLAY_W, self.DISPLAY_H = 500, 500
		self.display = pg.Surface((self.DISPLAY_W , self.DISPLAY_H))
		self.window = pg.display.set_mode(((self.DISPLAY_W , self.DISPLAY_H)))
		self.font_name = self.font_name = pg.font.get_default_font() #'8-BIT WONDER.TTF'
		self.BLACK, self.WHITE = (0,0,0), (255,255,255)
		self.curr_menu = MainMenu(self)


	def game_loop(self):
		while self.playing:
			self.check_events()
			if self.START_KEY:
				self.playing = False
			self.display.fill(self.BLACK)
			self.text_display('Thanks', 30, self.DISPLAY_W, self.DISPLAY_H)
			self.window.blit(self.display , (0,0))
			pg.display.update()
			self.reset_key()


	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.running, self.playing = False, False
				self.curr_menu.run_display == False
			if event.type == pg.KEYDOWN:
				
				if event.key == pg.K_RETURN:
					self.START_KEY = True
				if event.key == pg.K_BACKSPACE:
					self.BACK_KEY = True
				if event.key == pg.K_DOWN:
					self.DOWN_KEY = True
				if event.key == pg.K_UP:
					self.UP_KEY ==True

	def reset_keys(self):
		self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False

	def text_display(self, text, size, x, y):
		font = pg.font.Font(self.font_name,size)
		text_surface = font.render(text, True, self.WHITE)
		text_rect = text_surface.get_rect()
		text_rect.center = (x,y)
		self.display.blit(text_surface, text_rect)
