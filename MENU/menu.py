import pygame
import pygame_menu
pygame.init()
surface = pygame.display.set_mode((1000, 500))


def set_difficulty(value, difficulty):
    game = os.system("python main.py")
    print(game)
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu(300, 400, 'Plant vs Zombie')

menu.add_text_input('Name :', default='Name Here')
menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2),('',3)], onchange=set_difficulty)
menu.add_button('Launch the game', start_the_game,)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)