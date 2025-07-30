from Map import *
pygame.font.init()

screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

flip = True
aninum = 0
topy = 0
lowy = 0
playermovement = True
playerlife = True
playerx = 0
playery = 0
thirdeye = False

class Player:
    def __init__(self, x, y, hp, dmg, energy):
        global aninum
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
        self.vel = 5
        self.energy = energy
        self.maximum_health = self.hp
        self.maximum_energy = self.energy
        self.health_bar_lenght = 300
        self.energy_bar_lenght = 300
        self.animation1 = pygame.image.load('herosanimation/swordsmananimation/animation1.png').convert_alpha()
        self.animation1 = pygame.transform.scale(self.animation1, (100, 120))
        self.animation1_reverse = pygame.transform.flip(self.animation1, True, False)
        self.animation2 = pygame.image.load('herosanimation/swordsmananimation/animation2.png').convert_alpha()
        self.animation2 = pygame.transform.scale(self.animation2, (100, 120))
        self.animation2_reverse = pygame.transform.flip(self.animation2, True, False)
        self.animation3 = pygame.image.load('herosanimation/swordsmananimation/animation3.png').convert_alpha()
        self.animation3 = pygame.transform.scale(self.animation3, (100, 120))
        self.animation3_reverse = pygame.transform.flip(self.animation3, True, False)
        self.animation4 = pygame.image.load('herosanimation/swordsmananimation/animation4.png').convert_alpha()
        self.animation4 = pygame.transform.scale(self.animation4, (100, 120))
        self.animation4_reverse = pygame.transform.flip(self.animation4, True, False)
        self.animation_list = [self.animation1, self.animation2, self.animation3, self.animation4, self.animation3,
                               self.animation2]
        self.animation_list_reversed = [self.animation1_reverse, self.animation2_reverse, self.animation3_reverse,
                                        self.animation4_reverse, self.animation3_reverse, self.animation2_reverse]

        self.animation1thirdeye = pygame.image.load('herosanimation/swordsmananimationthirdeye/animation1.png').convert_alpha()
        self.animation1thirdeye = pygame.transform.scale(self.animation1thirdeye, (100, 120))
        self.animation1thirdeye_reverse = pygame.transform.flip(self.animation1thirdeye, True, False)
        self.animation2thirdeye = pygame.image.load('herosanimation/swordsmananimationthirdeye/animation2.png').convert_alpha()
        self.animation2thirdeye = pygame.transform.scale(self.animation2thirdeye, (100, 120))
        self.animation2thirdeye_reverse = pygame.transform.flip(self.animation2thirdeye, True, False)
        self.animation3thirdeye = pygame.image.load('herosanimation/swordsmananimationthirdeye/animation3.png').convert_alpha()
        self.animation3thirdeye = pygame.transform.scale(self.animation3thirdeye, (100, 120))
        self.animation3thirdeye_reverse = pygame.transform.flip(self.animation3thirdeye, True, False)
        self.animation4thirdeye = pygame.image.load('herosanimation/swordsmananimationthirdeye/animation4.png').convert_alpha()
        self.animation4thirdeye = pygame.transform.scale(self.animation4thirdeye, (100, 120))
        self.animation4thirdeye_reverse = pygame.transform.flip(self.animation4thirdeye, True, False)

        self.animationthirdeye_list = [self.animation1thirdeye, self.animation2thirdeye, self.animation3thirdeye, self.animation4thirdeye, self.animation3thirdeye,
                               self.animation2thirdeye]
        self.animationthirdeye_list_reversed = [self.animation1thirdeye_reverse, self.animation2thirdeye_reverse, self.animation3thirdeye_reverse,
                                        self.animation4thirdeye_reverse, self.animation3thirdeye_reverse, self.animation2thirdeye_reverse]

        self.attackanimation1 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation1.png').convert_alpha()
        self.attackanimation1 = pygame.transform.scale(self.attackanimation1, (100, 120))
        self.attackanimation1_reverse = pygame.transform.flip(self.attackanimation1, True, False)
        self.attackanimation2 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation2.png').convert_alpha()
        self.attackanimation2 = pygame.transform.scale(self.attackanimation2, (100, 120))
        self.attackanimation2_reverse = pygame.transform.flip(self.attackanimation2, True, False)
        self.attackanimation3 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation3.png').convert_alpha()
        self.attackanimation3 = pygame.transform.scale(self.attackanimation3, (100, 120))
        self.attackanimation3_reverse = pygame.transform.flip(self.attackanimation3, True, False)
        self.attackanimation4 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation3.png').convert_alpha()
        self.attackanimation4 = pygame.transform.scale(self.attackanimation3, (100, 120))
        self.attackanimation4_reverse = pygame.transform.flip(self.attackanimation3, True, False)
        self.attackanimation5 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation4.png').convert_alpha()
        self.attackanimation5 = pygame.transform.scale(self.attackanimation5, (100, 120))
        self.attackanimation5_reverse = pygame.transform.flip(self.attackanimation5, True, False)
        self.attackanimation6 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation5.png').convert_alpha()
        self.attackanimation6 = pygame.transform.scale(self.attackanimation6, (100, 120))
        self.attackanimation6_reverse = pygame.transform.flip(self.attackanimation6, True, False)
        self.attackanimation7 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation6.png').convert_alpha()
        self.attackanimation7 = pygame.transform.scale(self.attackanimation7, (100, 120))
        self.attackanimation7_reverse = pygame.transform.flip(self.attackanimation7, True, False)
        self.attackanimation8 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation7.png').convert_alpha()
        self.attackanimation8 = pygame.transform.scale(self.attackanimation8, (100, 120))
        self.attackanimation8_reverse = pygame.transform.flip(self.attackanimation8, True, False)
        self.attackanimation9 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation8.png').convert_alpha()
        self.attackanimation9 = pygame.transform.scale(self.attackanimation9, (100, 120))
        self.attackanimation9_reverse = pygame.transform.flip(self.attackanimation9, True, False)
        self.attackanimation10 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation9.png').convert_alpha()
        self.attackanimation10 = pygame.transform.scale(self.attackanimation10, (100, 120))
        self.attackanimation10_reverse = pygame.transform.flip(self.attackanimation10, True, False)
        self.attackanimation11 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimation/animation10.png').convert_alpha()
        self.attackanimation11 = pygame.transform.scale(self.attackanimation11, (100, 120))
        self.attackanimation11_reverse = pygame.transform.flip(self.attackanimation11, True, False)
        self.attackanimation_list = [self.attackanimation1, self.attackanimation2, self.attackanimation3,
                                     self.attackanimation4, self.attackanimation5, self.attackanimation6,
                                     self.attackanimation7, self.attackanimation8, self.attackanimation9, self.attackanimation10, self.attackanimation11,
                                     self.attackanimation10, self.attackanimation9,
                                     self.attackanimation8, self.attackanimation7
                                     ]
        self.attackanimation_list_reversed = [self.attackanimation1_reverse, self.attackanimation2_reverse,
                                              self.attackanimation3_reverse,
                                              self.attackanimation4_reverse, self.attackanimation5_reverse,
                                              self.attackanimation6_reverse, self.attackanimation7_reverse, self.attackanimation8_reverse,
                                              self.attackanimation9_reverse, self.attackanimation10_reverse, self.attackanimation11_reverse,
                                              self.attackanimation10_reverse, self.attackanimation9_reverse,
                                              self.attackanimation8_reverse, self.attackanimation7_reverse
                                              ]

        self.attackanimationthirdeye1 = pygame.image.load(
            'herosanimation/swordsmananimationthirdeye/animation1.png').convert_alpha()
        self.attackanimationthirdeye1 = pygame.transform.scale(self.attackanimationthirdeye1, (100, 120))
        self.attackanimationthirdeye1_reverse = pygame.transform.flip(self.attackanimationthirdeye1, True, False)
        self.attackanimationthirdeye2 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation2.png').convert_alpha()
        self.attackanimationthirdeye2 = pygame.transform.scale(self.attackanimationthirdeye2, (100, 120))
        self.attackanimationthirdeye2_reverse = pygame.transform.flip(self.attackanimationthirdeye2, True, False)
        self.attackanimationthirdeye3 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation3.png').convert_alpha()
        self.attackanimationthirdeye3 = pygame.transform.scale(self.attackanimationthirdeye3, (100, 120))
        self.attackanimationthirdeye3_reverse = pygame.transform.flip(self.attackanimationthirdeye3, True, False)
        self.attackanimationthirdeye4 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation3.png').convert_alpha()
        self.attackanimationthirdeye4 = pygame.transform.scale(self.attackanimationthirdeye3, (100, 120))
        self.attackanimationthirdeye4_reverse = pygame.transform.flip(self.attackanimationthirdeye3, True, False)
        self.attackanimationthirdeye5 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation4.png').convert_alpha()
        self.attackanimationthirdeye5 = pygame.transform.scale(self.attackanimationthirdeye5, (100, 120))
        self.attackanimationthirdeye5_reverse = pygame.transform.flip(self.attackanimationthirdeye5, True, False)
        self.attackanimationthirdeye6 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation5.png').convert_alpha()
        self.attackanimationthirdeye6 = pygame.transform.scale(self.attackanimationthirdeye6, (100, 120))
        self.attackanimationthirdeye6_reverse = pygame.transform.flip(self.attackanimationthirdeye6, True, False)
        self.attackanimationthirdeye7 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation6.png').convert_alpha()
        self.attackanimationthirdeye7 = pygame.transform.scale(self.attackanimationthirdeye7, (100, 120))
        self.attackanimationthirdeye7_reverse = pygame.transform.flip(self.attackanimationthirdeye7, True, False)
        self.attackanimationthirdeye8 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation7.png').convert_alpha()
        self.attackanimationthirdeye8 = pygame.transform.scale(self.attackanimationthirdeye8, (100, 120))
        self.attackanimationthirdeye8_reverse = pygame.transform.flip(self.attackanimationthirdeye8, True, False)
        self.attackanimationthirdeye9 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation8.png').convert_alpha()
        self.attackanimationthirdeye9 = pygame.transform.scale(self.attackanimationthirdeye9, (100, 120))
        self.attackanimationthirdeye9_reverse = pygame.transform.flip(self.attackanimationthirdeye9, True, False)
        self.attackanimationthirdeye10 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation9.png').convert_alpha()
        self.attackanimationthirdeye10 = pygame.transform.scale(self.attackanimationthirdeye10, (100, 120))
        self.attackanimationthirdeye10_reverse = pygame.transform.flip(self.attackanimationthirdeye10, True, False)
        self.attackanimationthirdeye11 = pygame.image.load(
            'herosanimation/swordsmanprimaryattackanimationthirdeye/animation10.png').convert_alpha()
        self.attackanimationthirdeye11 = pygame.transform.scale(self.attackanimationthirdeye11, (100, 120))
        self.attackanimationthirdeye11_reverse = pygame.transform.flip(self.attackanimationthirdeye11, True, False)
        self.attackanimationthirdeye_list = [self.attackanimationthirdeye1, self.attackanimationthirdeye2, self.attackanimationthirdeye3,
                                     self.attackanimationthirdeye4, self.attackanimationthirdeye5, self.attackanimationthirdeye6,
                                     self.attackanimationthirdeye7, self.attackanimationthirdeye8, self.attackanimationthirdeye9,
                                     self.attackanimationthirdeye10, self.attackanimationthirdeye11,
                                     self.attackanimationthirdeye10, self.attackanimationthirdeye9, self.attackanimationthirdeye8, self.attackanimationthirdeye7 ]
        self.attackanimationthirdeye_list_reversed = [self.attackanimationthirdeye1_reverse, self.attackanimationthirdeye2_reverse,
                                              self.attackanimationthirdeye3_reverse,
                                              self.attackanimationthirdeye4_reverse, self.attackanimationthirdeye5_reverse,
                                              self.attackanimationthirdeye6_reverse, self.attackanimationthirdeye7_reverse,
                                              self.attackanimationthirdeye8_reverse,
                                              self.attackanimationthirdeye9_reverse, self.attackanimationthirdeye10_reverse,
                                              self.attackanimationthirdeye11_reverse ,
                                     self.attackanimationthirdeye10_reverse, self.attackanimationthirdeye9_reverse,
                                                      self.attackanimationthirdeye8_reverse, self.attackanimationthirdeye7_reverse]

        self.specialattackanimation1 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation1.png').convert_alpha()
        self.specialattackanimation1 = pygame.transform.scale(self.specialattackanimation1, (100, 120))
        self.specialattackanimation1_reverse = pygame.transform.flip(self.specialattackanimation1, True, False)
        self.specialattackanimation2 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation2.png').convert_alpha()
        self.specialattackanimation2 = pygame.transform.scale(self.specialattackanimation2, (100, 120))
        self.specialattackanimation2_reverse = pygame.transform.flip(self.specialattackanimation2, True, False)
        self.specialattackanimation3 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation3.png').convert_alpha()
        self.specialattackanimation3 = pygame.transform.scale(self.specialattackanimation3, (100, 120))
        self.specialattackanimation3_reverse = pygame.transform.flip(self.specialattackanimation3, True, False)
        self.specialattackanimation4 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation3.png').convert_alpha()
        self.specialattackanimation4 = pygame.transform.scale(self.specialattackanimation3, (100, 120))
        self.specialattackanimation4_reverse = pygame.transform.flip(self.specialattackanimation3, True, False)
        self.specialattackanimation5 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation4.png').convert_alpha()
        self.specialattackanimation5 = pygame.transform.scale(self.specialattackanimation5, (100, 120))
        self.specialattackanimation5_reverse = pygame.transform.flip(self.specialattackanimation5, True, False)
        self.specialattackanimation6 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation5.png').convert_alpha()
        self.specialattackanimation6 = pygame.transform.scale(self.specialattackanimation6, (100, 120))
        self.specialattackanimation6_reverse = pygame.transform.flip(self.specialattackanimation6, True, False)
        self.specialattackanimation7 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation6.png').convert_alpha()
        self.specialattackanimation7 = pygame.transform.scale(self.specialattackanimation7, (100, 120))
        self.specialattackanimation7_reverse = pygame.transform.flip(self.specialattackanimation7, True, False)
        self.specialattackanimation8 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation7.png').convert_alpha()
        self.specialattackanimation8 = pygame.transform.scale(self.specialattackanimation8, (100, 120))
        self.specialattackanimation8_reverse = pygame.transform.flip(self.specialattackanimation8, True, False)
        self.specialattackanimation9 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation8.png').convert_alpha()
        self.specialattackanimation9 = pygame.transform.scale(self.specialattackanimation9, (100, 120))
        self.specialattackanimation9_reverse = pygame.transform.flip(self.specialattackanimation9, True, False)
        self.specialattackanimation10 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation9.png').convert_alpha()
        self.specialattackanimation10 = pygame.transform.scale(self.specialattackanimation10, (100, 120))
        self.specialattackanimation10_reverse = pygame.transform.flip(self.specialattackanimation10, True, False)
        self.specialattackanimation11 = pygame.image.load(
            'herosanimation/swordsmanspecialattackanimation/animation10.png').convert_alpha()
        self.specialattackanimation11 = pygame.transform.scale(self.specialattackanimation11, (100, 120))
        self.specialattackanimation11_reverse = pygame.transform.flip(self.specialattackanimation11, True, False)
        self.specialattackanimation_list = [self.specialattackanimation1, self.specialattackanimation2, self.specialattackanimation3,
                                     self.specialattackanimation4, self.specialattackanimation5, self.specialattackanimation6,
                                     self.specialattackanimation7, self.specialattackanimation8, self.specialattackanimation9,
                                     self.specialattackanimation10, self.specialattackanimation11,
                                     self.specialattackanimation10, self.specialattackanimation9,
                                     self.specialattackanimation8, self.specialattackanimation7
                                     ]
        self.specialattackanimation_list_reversed = [self.specialattackanimation1_reverse, self.specialattackanimation2_reverse,
                                              self.specialattackanimation3_reverse,
                                              self.specialattackanimation4_reverse, self.specialattackanimation5_reverse,
                                              self.specialattackanimation6_reverse, self.specialattackanimation7_reverse,
                                              self.specialattackanimation8_reverse,
                                              self.specialattackanimation9_reverse, self.specialattackanimation10_reverse,
                                              self.specialattackanimation11_reverse,
                                              self.specialattackanimation10_reverse, self.specialattackanimation9_reverse,
                                              self.specialattackanimation8_reverse, self.specialattackanimation7_reverse]

        self.img = self.animation_list[int(aninum)]
        self.img = pygame.transform.scale(self.img, (100, 120))
        self.player_rect = pygame.Rect((self.x, self.y),(100, 120))
        self.player_surface = pygame.Surface([100, 120])
        self.screen = screen
        self.youdied = pygame.image.load('photos/gameoverphoto.png')
        self.youdied = pygame.transform.scale(self.youdied,(1280, 720))
        self.font2 = pygame.font.Font('font/Decay-M5RB.ttf', 28)
        self.skillstab = pygame.image.load('photos/herotab.png').convert_alpha()
        self.skillstab = pygame.transform.scale(self.skillstab, (1100, 250))



    def movement(self):
        global flip, aninum, hp, playermovement, thirdeye, playerx, playery
        self.keys = pygame.key.get_pressed()
        playerx = self.player_rect.x
        playery = self.player_rect.y
        self.player_rect.x = playerx
        self.player_rect.y = playery

        if self.keys[pygame.K_RIGHT] and self.player_rect.x < 1160 and playermovement:
            flip = True
            self.player_rect.x += self.vel
            if thirdeye:
                self.img = self.animationthirdeye_list[int(aninum)]
            else:
                self.img = self.animation_list[int(aninum)]
            if aninum < len(self.animation_list) - 1:
                aninum += 0.3
            elif aninum >= len(self.animation_list)- 1:
                aninum = 0


        if self.keys[pygame.K_LEFT] and self.player_rect.x > 20 and playermovement:
            flip = False
            self.player_rect.x -= self.vel
            if thirdeye:
                self.img = self.animationthirdeye_list_reversed[int(aninum)]
            else:
                self.img = self.animation_list_reversed[int(aninum)]
            if aninum < len(self.animation_list) - 1:
                aninum += 0.3
            elif aninum >= len(self.animation_list) - 1:
                aninum = 0

            if flip >= 1:
                flip = 0

        if self.keys[pygame.K_UP] and playermovement and self.player_rect.y > 50:

            if self.keys[pygame.K_LEFT] or self.keys[pygame.K_RIGHT]:
                self.player_rect.y -= 3

            else:
                self.player_rect.y -= self.vel
                if flip >= 1:
                    if thirdeye:
                        self.img = self.animationthirdeye_list[int(aninum)]
                    else:
                        self.img = self.animation_list[int(aninum)]
                elif flip < 1:
                    if thirdeye:
                        self.img = self.animationthirdeye_list_reversed[int(aninum)]
                    else:
                        self.img = self.animation_list_reversed[int(aninum)]

                if aninum < len(self.animation_list) - 1:
                    aninum += 0.3
                elif aninum >= len(self.animation_list) - 1:
                    aninum = 0

        if self.keys[pygame.K_DOWN] and playermovement and self.player_rect.y < 500:

            if self.keys[pygame.K_LEFT] or self.keys[pygame.K_RIGHT]:
                self.player_rect.y += 3

            else:
                self.player_rect.y += self.vel
                if flip >= 1:
                    if thirdeye:
                        self.img = self.animationthirdeye_list[int(aninum)]
                    else:
                        self.img = self.animation_list[int(aninum)]
                elif flip < 1:
                    if thirdeye:
                        self.img = self.animationthirdeye_list_reversed[int(aninum)]
                    else:
                        self.img = self.animation_list_reversed[int(aninum)]

                if aninum < len(self.animation_list) - 1:
                    aninum += 0.3
                elif aninum >= len(self.animation_list) - 1:
                    aninum = 0

        if self.keys[pygame.K_o]:
            if self.hp > 0:
                self.hp -= 1
        if self.keys[pygame.K_i]:
            if self.hp < self.maximum_health:
                self.hp += 1

        self.update()
    def player_render(self):
        self.screen.blit(self.img,(self.player_rect.x, self.player_rect.y))
        self.screen.blit(self.skillstab, (90, 500))

    def updatexy_map2(self):
        self.player_rect.x = 100
        self.player_rect.y = 300

    def takedamage(self):
        if self.player_rect.x > 500:
            self.hp -= 1

    def player_health_bar(self):
        self.font = pygame.font.Font('font/Decay-M5RB.ttf', 28)
        self.health_text = self.font.render('HEALTH',True,(255, 0, 0))
        self.health_ratio = self.maximum_health / self.health_bar_lenght
        self.screen.blit(self.health_text,(255, 615))

    def update(self):
        self.player_rect = pygame.Rect((self.player_rect.x, self.player_rect.y),(100, 120))



    def player_energy_bar(self):
        self.font = pygame.font.Font('font/Decay-M5RB.ttf', 28)
        self.energy_text = self.font.render('ENERGY', True, (242, 255, 0))
        self.energy_ratio = self.maximum_energy / self.energy_bar_lenght
        self.screen.blit(self.energy_text, (835, 615))

    def player_health_bar_render(self):
        self.current_health = self.hp
        pygame.draw.rect(self.screen,(255, 0, 0),(200, 580, self.current_health/self.health_ratio, 25))
        pygame.draw.rect(self.screen,(255, 255, 255),(200, 580, self.health_bar_lenght, 25), 4)

    def player_energy_bar_render(self):
        self.current_energy = self.energy
        pygame.draw.rect(self.screen,(242, 255, 0),(783, 580, self.current_energy/self.energy_ratio, 25))
        pygame.draw.rect(self.screen,(255, 255, 255),(783, 580, self.energy_bar_lenght, 25), 4)

    def player_energy_regeneration(self):
        if self.energy < self.maximum_energy:
            self.energy += 0.1


    def PlayerDied(self):
        global playerlife
        if self.hp <= 0:
            playerlife = False
            self.screen.blit(self.youdied,(0,0))








