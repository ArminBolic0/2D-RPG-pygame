import Player
import pygame

attackanimation = 0
attackflag = False
dashflag = False
dashcooldown = False
dashcooldowncounter = 0
dashduration = 100
thirdeyeflag = False
thirdeyecooldown = False
thirdeyecooldowncounter = 0
thirdeyeduration = 200
specialattackflag = False
specialattackcooldown = False
specialattackcooldowncounter = 0



class Swordsman(Player.Player):
    def primary_skill(self):
        global specialattackflag, attackflag, attackanimation, aninum, dashflag, dashcooldown, dashcooldowncounter, dashduration, thirdeyeflag, thirdeyecooldown, thirdeyecooldowncounter, thirdeyeduration
        self.f = pygame.font.Font('font/BALLOON DREAMS.ttf', 20)
        self.dashused = pygame.image.load('photos/DashCooldown.png')
        self.dashused = pygame.transform.scale(self.dashused, (35, 35))
        self.thirdeyeused = pygame.image.load('photos/Thirdeyecooldown.png')
        self.thirdeyeused = pygame.transform.scale(self.thirdeyeused, (35, 35))
        self.dashcooldowntext = self.f.render(str(int(dashcooldowncounter)), True, (255, 255, 255))
        self.thirdeyecooldowntext = self.f.render(str(int(thirdeyecooldowncounter)), True, (255, 255, 255))
        self.primary_skill_rect = pygame.Rect((self.player_rect.x + 80, self.player_rect.y + 50),(50, 60))
        self.primary_skill_surface = pygame.Surface([50, 100])
        if self.keys[pygame.K_q]:
            if self.energy >= 10:
                if   Player.flip:
                    if attackanimation == 0:
                        attackflag = True
                        self.energy -= 10
                    self.primary_skill_animation()
                elif Player.flip == False:
                    if attackanimation == 0:
                        attackflag = True
                        self.energy -= 10
                    self.primary_skill_animation()

        if self.keys[pygame.K_r]:
            if self.energy >= 70:
                if  Player.flip:
                    if attackanimation == 0:
                        specialattackflag = True
                        self.energy -= 70
                elif Player.flip == False:
                    if attackanimation == 0:
                        specialattackflag = True
                        self.energy -= 70

        if specialattackflag:
            self.special_skill_animation()

        if self.keys[pygame.K_w] and not dashcooldown:
            dashflag = True

        if dashduration > 0 and dashflag:
            dashduration -= 0.5
            dashcooldowncounter = 10
            self.vel = 20
        elif dashduration <= 0:
            dashflag = False

        if dashcooldowncounter > 0 and dashduration <= 0:
            self.screen.blit(self.dashused, (660, 577))
            if dashcooldowncounter >= 10:
                self.screen.blit(self.dashcooldowntext, (667, 578))
            else:
                self.screen.blit(self.dashcooldowntext, (671, 578))
            dashcooldown = True
            dashcooldowncounter -= 0.02
            self.vel = 5

        elif dashcooldowncounter <= 0:
            dashcooldown = False
            dashduration = 5



        if self.keys[pygame.K_e] and not thirdeyecooldown:
            thirdeyeflag = True

        if thirdeyeduration > 0 and thirdeyeflag:
            thirdeyeduration -= 0.3
            if thirdeyecooldowncounter <= 0:
                thirdeyecooldowncounter = 45
            Player.thirdeye = True

        elif thirdeyeduration <= 0:
            thirdeyeflag = False
            Player.thirdeye = False



        if thirdeyecooldowncounter > 0:
            thirdeyecooldowncounter -= 0.02
            self.atk = 100
            self.screen.blit(self.thirdeyeused, (725, 577))
            if thirdeyecooldowncounter >= 10:
                self.screen.blit(self.thirdeyecooldowntext, (730, 578))
            else:
                self.screen.blit(self.thirdeyecooldowntext, (735, 578))
            thirdeyecooldown = True

        if thirdeyecooldowncounter <= 0:
            thirdeyecooldown = False
            thirdeyeduration = 300








    def primary_skill_animation(self):
        global attackanimation, attackflag

        if attackflag:
            if Player.thirdeye:
                if Player.flip:
                    if attackanimation < 15:
                        Player.playermovement = False
                        self.img = self.attackanimationthirdeye_list[int(attackanimation)]
                        attackanimation += 0.5
                    elif attackanimation >= 15:
                        Player.playermovement = True
                        attackflag = False
                        attackanimation = 0
                        self.img = self.attackanimationthirdeye1
                elif Player.flip == False:
                    if attackanimation < 15:
                        Player.playermovement = False
                        self.img = self.attackanimationthirdeye_list_reversed[int(attackanimation)]
                        attackanimation += 0.5
                    elif attackanimation == 15:
                        Player.playermovement = True
                        attackflag = False
                        attackanimation = 0
                        self.img = self.attackanimationthirdeye1_reverse

            else:
                if Player.flip:
                    if attackanimation < 15:
                        Player.playermovement = False
                        self.img = self.attackanimation_list[int(attackanimation)]
                        attackanimation += 0.5
                    elif attackanimation >= 15:
                        Player.playermovement = True
                        attackflag = False
                        attackanimation = 0
                        self.img = self.attackanimation1
                elif Player.flip == False:
                    if attackanimation < 15:
                        Player.playermovement = False
                        self.img = self.attackanimation_list_reversed[int(attackanimation)]
                        attackanimation += 0.5
                    elif attackanimation == 15:
                        Player.playermovement = True
                        attackflag = False
                        attackanimation = 0
                        self.img = self.attackanimation1_reverse

    def special_skill_animation(self):
        global specialattackflag, specialattackcooldown, specialattackcooldowncounter, attackanimation

        if specialattackflag:
            if Player.flip:
                if attackanimation < 15:
                    Player.playermovement = False
                    self.img = self.specialattackanimation_list[int(attackanimation)]
                    attackanimation += 0.5
                elif attackanimation >= 15:
                    Player.playermovement = True
                    attackanimation = 0
                    specialattackflag = False
                    self.img = self.attackanimation1
            elif Player.flip == False:
                if attackanimation < 15:
                    Player.playermovement = False
                    self.img = self.specialattackanimation_list_reversed[int(attackanimation)]
                    attackanimation += 0.5
                elif attackanimation == 15:
                    Player.playermovement = True
                    attackanimation = 0
                    specialattackflag = False
                    self.img = self.attackanimation1_reverse















