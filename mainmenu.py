import pygame
import os
import pygame_menu
from pygame_menu import sound 
pygame.init()
surface = pygame.display.set_mode((1000, 500))


def set_difficulty(value, difficulty):
    pass	
def set_volume():
	engine = sound.Sound()
	mouse_click = 'Resoures/sound_track/Mouse-Click-DoubleClick-00-c-FesliyanStudios.com.mp3'
	open_menu = 'Resoures/sound_track/butter_openmenu.mp3'
	engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, mouse_click )
	engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, open_menu)
 
 
def option_the_game():
	option = pygame_menu.Menu(500, 1000, 'DEMO',theme = mytheme)
	option.add_button('Volume', set_volume)
	option.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2),('',3)], onchange=set_difficulty)
	
def start_the_game():
    game = os.system("python main.py")
    print(game)

def quit_the_game():
	pygame_menu.events.EXIT()




mytheme = pygame_menu.themes.THEME_ORANGE.copy()

mytheme.title_background_color=(0, 0, 0)
mytheme.background_color=(0, 10, 0, 25)


font = pygame_menu.font.FONT_NEVIS
mytheme.widget_font = font

myimage = pygame_menu.baseimage.BaseImage(image_path='Resources/bgmenu.png', drawing_mode = pygame_menu.baseimage.IMAGE_MODE_SIMPLE)
mytheme.background_color = myimage
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE	
print(mytheme)


menu = pygame_menu.Menu(500, 1000, 'DEMO',theme = mytheme)

soundv = sound.Sound()

#menu.add_text_input('Name :', default='Name Here')
#menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2),('',3)], onchange=set_difficulty)

soundv.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'Resoures/-sound_track/Mouse-Click-DoubleClick-00-c-FesliyanStudios.com.mp3' )
soundv.set_sound(sound.SOUND_TYPE_OPEN_MENU, 'Resoures/-sound_track/butter_openmenu.mp3')
 
menu.add_button('Play Trial', start_the_game)
menu.add_button('Option', option_the_game)
menu.add_button('?!? Quit ?!?', pygame_menu.events.EXIT)
menu.mainloop(surface)

#python3 mainmenu.py
