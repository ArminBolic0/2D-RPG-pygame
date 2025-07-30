import Map
from Swordsman import *
from GameLoop import WIDTH, HEIGHT, screen
from pygame import mixer
import Player
import GameLoading
mixer.init()

number = 0
pygame.init()

map1 = Map.Maps('maps/map1.jpg', WIDTH, HEIGHT, screen)
ingamemenuflag = False
gameeventflag = False
game = False
p1 = Swordsman(300, 300, 100, 50, 100)


class Game_Logic:
    def IngameMenu(self):
        global ingamemenuflag, game
        self.ingamemenu = pygame.image.load('photos/ingamemainmenu.png')
        self.ingamemenu = pygame.transform.scale(self.ingamemenu,(1280, 720))
        screen.blit(self.ingamemenu,(0,0))
        self.x, self.y = pygame.mouse.get_pos()
        self.mright, self.mmiddle, self.mleft = pygame.mouse.get_pressed()
        if self.mright:
            print(self.x, self.y)
        if self.mright:
            if self.x in range(503, 781) and self.y in range(361, 411):
                ingamemenuflag = False
            if self.x in range(231, 1061) and self.y in range(485, 540):
                game = False
                ingamemenuflag = False
                Map.map1 = True
                Map.map2 = False
                Map.map3 = False
                Map.map4 = False




    def Game_Main(self):
        global ingamemenuflag, number, gameeventflag
        gameeventflag = True
        self.keys = pygame.key.get_pressed()
        if not Map.map2resetflag and Map.map2:
            p1.updatexy_map2()
        if not Map.map3resetflag and Map.map3:
            p1.updatexy_map2()
        if not Map.map4resetflag and Map.map4:
            p1.updatexy_map2()
        if self.keys[pygame.K_ESCAPE] and Player.playerlife == True and not ingamemenuflag:
            ingamemenuflag = True
        if GameLoading.loadingflag:
            GameLoading.loading_bar_render()

        else:
            if not ingamemenuflag :
                p1.movement()
                map1.Map_Render()
                p1.player_render()
                p1.player_health_bar()
                p1.player_health_bar_render()
                p1.player_energy_bar()
                p1.player_energy_bar_render()
                p1.player_energy_regeneration()
                p1.primary_skill_animation()
                p1.PlayerDied()
                p1.primary_skill()


            elif ingamemenuflag:
                self.IngameMenu()






