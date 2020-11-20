import pygame
import os
import pygame_menu
pygame.init()
surface = pygame.display.set_mode((1000, 500))


#def set_difficulty(value, difficulty):
    #pass	
    

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

myimage = pygame_menu.baseimage.BaseImage(
    image_path='Resources/bgmenu.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_SIMPLE
)
mytheme.background_color = myimage
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE	
print(mytheme)


menu = pygame_menu.Menu(500, 1000, 'DEMO',theme = mytheme)

#menu.add_text_input('Name :', default='Name Here')
#menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2),('',3)], onchange=set_difficulty)
menu.add_button('Play Trial', start_the_game)

menu.add_button('?!? Quit ?!?', pygame_menu.events.EXIT)
menu.mainloop(surface)