import pygame
from Game import screen
import LoginRegister

class Ranks:
    def __init__(self):
        self.ranking_info = pygame.image.load('ranks/ranks.png')
        self.ranking_info = pygame.transform.scale(self.ranking_info,(1280, 720))
        self.bronze = pygame.image.load('ranks/Bronze.png')
        self.bronze = pygame.transform.scale(self.bronze,(215, 180))
        self.silver = pygame.image.load('ranks/Silver.png')
        self.silver = pygame.transform.scale(self.silver, (215, 180))
        self.ruby = pygame.image.load('ranks/Ruby.png')
        self.ruby = pygame.transform.scale(self.ruby, (215, 180))
        self.imperial = pygame.image.load('ranks/Imperial.png')
        self.imperial = pygame.transform.scale(self.imperial, (215, 180))
        self.legend = pygame.image.load('ranks/Legend.png')
        self.legend = pygame.transform.scale(self.legend, (215, 180))
        self.champion = pygame.image.load('ranks/Champion.png')
        self.champion = pygame.transform.scale(self.champion, (215, 180))
        self.ranks = False

    def Ranks_Logic(self):
        global poeni
        self.x, self.y = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()
        self.keys = pygame.key.get_pressed()
        self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 18)
        self.points = self.font.render(f'Your current points: {LoginRegister.loggedinpoints}', True, (255, 255, 255))
        self.nickname = self.font.render(LoginRegister.loggedinnickname, True, (255, 255, 255))
        screen.blit(self.nickname, (1050, 420))
        screen.blit(self.points, ((930, 460)))
        if self.keys[pygame.K_UP]:
            LoginRegister.loggedinpoints += 5

        if LoginRegister.loggedinpoints >= 0 and LoginRegister.loggedinpoints <= 500:
            screen.blit(self.bronze,(980, 500))
            self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 25)
            self.bronze_text = self.font.render("BRONZE", True, (130, 114, 33))
            screen.blit(self.bronze_text,(1030, 670))

        if LoginRegister.loggedinpoints > 500 and LoginRegister.loggedinpoints <= 700:
            screen.blit(self.silver,(980, 500))
            self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 25)
            self.silver_text = self.font.render("SILVER", True, (163, 161, 149))
            screen.blit(self.silver_text, (1040, 670))

        if LoginRegister.loggedinpoints > 700 and LoginRegister.loggedinpoints <= 1000:
            screen.blit(self.ruby,(980, 500))
            self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 25)
            self.ruby_text = self.font.render("RUBY", True, (173, 72, 38))
            screen.blit(self.ruby_text, (1050, 670))

        if LoginRegister.loggedinpoints > 1000 and LoginRegister.loggedinpoints <= 1300:
            screen.blit(self.imperial,(980, 500))
            self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 25)
            self.imperial_text = self.font.render("IMPERIAL", True, (158, 25, 156))
            screen.blit(self.imperial_text, (1030, 670))

        if LoginRegister.loggedinpoints > 1300 and LoginRegister.loggedinpoints <= 2000:
            screen.blit(self.legend,(980, 500))
            self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 25)
            self.legend_text = self.font.render("LEGEND", True, (112, 189, 196))
            screen.blit(self.legend_text, (1035, 670))

        if LoginRegister.loggedinpoints > 2000:
            screen.blit(self.champion,(980, 500))
            self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 25)
            self.champion_text = self.font.render("CHAMPION", True, (176, 12, 12))
            screen.blit(self.champion_text, (1020, 670))

        if self.x in range(980, 1180) and self.y in range(516, 670):
            if self.mouseleft:
                self.ranks = True

        if self.ranks:
            screen.blit(self.ranking_info,(0, 0))
            if self.keys[pygame.K_ESCAPE]:
                self.ranks = False


ranks = Ranks()