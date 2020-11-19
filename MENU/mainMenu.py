try:
	from game import Game

	g = Game()	

	while g.running:
		g.curr_menu.display_menu()
		g.game_loop()

except Exception as Bug:
	print(Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()