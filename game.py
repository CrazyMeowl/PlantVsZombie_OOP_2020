import pygame as pg
class Game():
	def __init__(self):
		pg.init()
		self.running , self.playing = True, False
		self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False
		self.DISPLAY_W, self.DISPLAY_H = 480, 270
		self.display = pg.Surface((self.DISPLAY_W , self.DISPLAY_H))
		self.window = pg.display.set_mode(((self.DISPLAY_W , self.DISPLAY_H)))
		self.font_name = pg.font.get_default_font() #'8-BIT WONDER.TTF'
		self.BLACK, self.WHITE = (0,0,0), (255,255,255)


	def game_loop(self):
		while self.playing:
			self.check_events()
			if self.START_KEY:
				self.playing = False
			self.display.fill(self.WHITE)
			self.window.blit(self.display , (0,0))
			self.text_display('Thanks', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)

			pg.display.update()
			self.reset_key()


	def check_Action(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.running, self.playing = False, False
			if event.type == pg.KEYDOWN:
				
				if event.key == pg.K_RETURN:
					self.START_KEY = True
				if event.key == pg.K_BACKSPACE:
					self.BACK_KEY = True
				if event.key == pg.K_DOWN:
					self.DOWN_KEY = True
				if event.key == pg.K_UP:
					self.UP_KEY ==True

	def reset_key(self):
		self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False

	def text_display(self, text, size, x, y):
		font = pg.font.Font(self.font_name,size)
		text_surface = font.render(text, True, self.BLACK)
		text_rectangle = text_surface.get_rect()
		text_rectangle.center = (x,y)
		self.display.blit(text_surface, text_rectangle)
