import pygame
import Player

map1 = True
map2 = False
map2resetflag = False
map3 = False
map3resetflag = False
map4 = False
map4resetflag = False


class Maps:
    def __init__(self, map, w, h, screen):
        self.screen = screen
        self.w = w
        self.h = h
        self.map1 = pygame.image.load(map)
        self.map1 = pygame.transform.scale(self.map1,(self.w, self.h))
        self.map2 = pygame.image.load('maps/map2.jpg')
        self.map2 = pygame.transform.scale(self.map2, (self.w, self.h))
        self.map3 = pygame.image.load('maps/map3.jpg')
        self.map3 = pygame.transform.scale(self.map3, (self.w, self.h))
        self.map4 = pygame.image.load('maps/map4.jpg')
        self.map4 = pygame.transform.scale(self.map4, (self.w, self.h))
        self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 18)
        self.press = self.font.render("PRESS F TO INTERACT", True, (255, 255, 255))


    def Map_Render(self):
        global map1, map2, map3, map4, map2resetflag, map3resetflag, map4resetflag
        self.keys = pygame.key.get_pressed()
        if map1:
            self.screen.blit(self.map1,(0,0))
            if Player.playerx in range(540, 655) and Player.playery < 70:
                self.screen.blit(self.press,(520, 480))
                if self.keys[pygame.K_f]:
                    map1 = False
                    map2 = True
        elif map2:
            self.screen.blit(self.map2, (0, 0))
            if Player.playerx > 1100:
                map3 = True
                map2 = False
            map2resetflag = True
        elif map3:
            self.screen.blit(self.map3, (0, 0))
            map3resetflag = True
            map2resetflag = False
            if Player.playerx > 1140 and Player.playery < 70:
                self.screen.blit(self.press,(520, 480))
                if self.keys[pygame.K_f]:
                    map3 = False
                    map4 = True
            if Player.playerx < 100:
                map3 = False
                map2 = True
        elif map4:
            self.screen.blit(self.map4, (0, 0))
            map4resetflag = True
            map3resetflag = False
