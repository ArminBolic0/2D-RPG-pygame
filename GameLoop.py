import sys
from MainMenu import *
from LoginRegister import *
from AdminPage import *
import Game

WIDTH = 1280
HEIGHT = 720
icon = pygame.image.load('photos/knight.png')
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
e = 0
eventi = ""


class GameLoop:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Hero Quest')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.Menu = MainMenu(screen)
        self.Login = Login(screen)

    def run(self):
        global loginflag, email, e, eventi
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if not Game.gameeventflag:
                self.event = pygame.event.wait(3000)
                self.Menu.get_event(self.event)
            screen.fill('black')
            self.Login.login_register_logic(self.event)
            self.Menu.MainMenu_Logic()
            pygame.display.update()
            self.clock.tick(FPS)







if __name__ == '__main__':
    game = GameLoop()
    game.run()




