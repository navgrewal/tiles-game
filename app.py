from login_signup import main_screen
main_screen()

from loggeduser import loggedUser

if (loggedUser):
    from game import *
    game_screen()