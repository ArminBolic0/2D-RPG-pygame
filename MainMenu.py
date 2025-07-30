import pygame

import Game
from Ranking import *
from SoundSystem import *
import LoginRegister
import Leaderboards
import AdminPage
import GameLoading

pygame.init()

adminpageflag = False
mainmenuflag = False
heroselectionflag = False
swordsmaninfoflag = False
elfinfoflag = False
darkmageinfoflag = False
demonhunterinfoflag = False
swordsmanskillsflag = False
elfskillsflag = False
darkmageskillsflag = False
demonhunterskillsflag = False
gameflag = True
leaderboardflag = False
options = False
volume = True
counter = 0

nb = 0

class MainMenu:
    def __init__(self, screen):
        # background photo
        self.option = pygame.image.load('photos/options.jpg')
        self.option = pygame.transform.scale(self.option, (1280, 720))
        self.background = pygame.image.load('photos/background7.jpg').convert()
        self.background = pygame.transform.scale(self.background, (1280, 720))
        self.backgroundstart = pygame.image.load('photos/backgroundstart.jpg').convert()
        self.backgroundstart = pygame.transform.scale(self.backgroundstart, (1280, 720))
        self.backgroundoptions = pygame.image.load('photos/backgroundoptions.jpg').convert()
        self.backgroundoptions = pygame.transform.scale(self.backgroundoptions, (1280, 720))
        self.backgroundexit = pygame.image.load('photos/backgroundexit.jpg').convert()
        self.backgroundexit = pygame.transform.scale(self.backgroundexit, (1280, 720))
        self.backgroundadmin = pygame.image.load('photos/background7admin.jpg').convert()
        self.backgroundadmin = pygame.transform.scale(self.backgroundadmin, (1280, 720))
        self.background7startadmin = pygame.image.load('photos/background7startadmin.jpg').convert()
        self.background7startadmin = pygame.transform.scale(self.background7startadmin, (1280, 720))
        self.background7optionsadmin = pygame.image.load('photos/background7optionsadmin.jpg').convert()
        self.background7optionsadmin = pygame.transform.scale(self.background7optionsadmin, (1280, 720))
        self.background7exitadmin = pygame.image.load('photos/background7exitadmin.jpg').convert()
        self.background7exitadmin = pygame.transform.scale(self.background7exitadmin, (1280, 720))
        self.screen = screen
        self.Game_Run = Game.Game_Logic()


    def mainmenu_render(self):
        if AdminPage.adminflag:
            self.screen.blit(self.backgroundadmin, (0, 0))
        if AdminPage.adminflag == False:
            self.screen.blit(self.background, (0, 0))

    def hero_selection(self):
        global swordsmaninfoflag, mainmenuflag, heroselectionflag, elfinfoflag, demonhunterinfoflag, darkmageinfoflag
        self.x, self.y = pygame.mouse.get_pos()
        self.heroselection = pygame.image.load('photos/heroselection.png')
        self.heroselection = pygame.transform.scale(self.heroselection, (1280, 720))
        self.screen.blit(self.heroselection, (0, 0))
        self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 25)
        self.keys = pygame.key.get_pressed()
        self.demomessage = self.font.render("CURRENTLY NOT AVAILABLE", True, (255, 255, 255))
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()

        if self.keys[pygame.K_ESCAPE]:
            mainmenuflag = True
            heroselectionflag = False

        if self.x in range(86, 268) and self.y in range(237, 406):
            if self.mouseleft:
                mainmenuflag = False
                heroselectionflag = False
                swordsmaninfoflag = True

        if self.x in range(409, 553) and self.y in range(237, 406):
            if self.mouseleft:
                self.screen.blit(self.demomessage, (430, 170))

        if self.x in range(668, 822) and self.y in range(237, 406):
            if self.mouseleft:
                self.screen.blit(self.demomessage, (430, 170))

        if self.x in range(991, 1138) and self.y in range(237, 406):
            if self.mouseleft:
                self.screen.blit(self.demomessage, (430, 170))

    def swordsman_info_render(self):
        global swordsmanskillsflag, swordsmaninfoflag
        self.swordsmaninfo = pygame.image.load('photos/swordsmaninfo.png')
        self.swordsmaninfo = pygame.transform.scale(self.swordsmaninfo, (1280, 720))
        self.screen.blit(self.swordsmaninfo,(0,0))
        self.x, self.y = pygame.mouse.get_pos()
        self.mousebutton = pygame.mouse.get_pressed(3)

        if self.x in range(376, 677) and self.y in range(656, 691):
            if self.mouseleft:
                swordsmaninfoflag = False
                swordsmanskillsflag = True


    def elf_info_render(self):
        global elfinfoflag, elfskillsflag
        self.elfinfo = pygame.image.load('photos/elfinfo.png')
        self.elfinfo = pygame.transform.scale(self.elfinfo, (1280, 720))
        self.screen.blit(self.elfinfo,(0,0))

    def darkmage_info_render(self):
        global darkmageskillsflag, darkmageinfoflag
        self.darkmageinfo = pygame.image.load('photos/darkmageinfo.png')
        self.darkmageinfo = pygame.transform.scale(self.darkmageinfo, (1280, 720))
        self.screen.blit(self.darkmageinfo,(0,0))

    def demonhunter_info_render(self):
        global demonhunterinfoflag, demonhunterskillsflag
        self.demonhunterinfo = pygame.image.load('photos/demonhunterinfo.png')
        self.demonhunterinfo = pygame.transform.scale(self.demonhunterinfo, (1280, 720))
        self.screen.blit(self.demonhunterinfo,(0,0))
        self.x, self.y = pygame.mouse.get_pos()

    def demonhunter_skills_render(self):
        self.demonhunterskills = pygame.image.load('photos/demonhunterskills.png')
        self.demonhunterskills = pygame.transform.scale(self.demonhunterskills,(1280, 720))
        self.screen.blit(self.demonhunterskills,(0,0))

    def swordsman_skills_render(self):
        self.swordsmanskills = pygame.image.load('photos/swordsmanskills.png')
        self.swordsmanskills = pygame.transform.scale(self.swordsmanskills,(1280, 720))
        self.screen.blit(self.swordsmanskills,(0,0))

    def elf_skills_render(self):
        self.elfskills = pygame.image.load('photos/elfskills.png')
        self.elfskills = pygame.transform.scale(self.elfskills,(1280, 720))
        self.screen.blit(self.elfskills,(0,0))

    def darkmage_skills_render(self):
        self.darkmageskills = pygame.image.load('photos/darkmageskills.png')
        self.darkmageskills = pygame.transform.scale(self.darkmageskills,(1280, 720))
        self.screen.blit(self.darkmageskills,(0,0))

    def start_goback(self):
        global heroselectionflag, swordsmaninfoflag, elfinfoflag, darkmageinfoflag, demonhunterinfoflag, swordsmanskillsflag, elfskillsflag, darkmageskillsflag, demonhunterskillsflag
        self.x, self.y = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()
        if self.x in range(62, 277) and self.y in range(620, 694):
            if self.mouseleft:
                heroselectionflag = True
                swordsmaninfoflag = False
                elfinfoflag = False
                darkmageinfoflag = False
                demonhunterinfoflag = False
                swordsmanskillsflag = False
                elfskillsflag = False
                darkmageskillsflag = False
                demonhunterskillsflag = False

    def mainmenu_select(self):
        global heroselectionflag, mainmenuflag, nb, leaderboardflag, adminpageflag, options
        self.x, self.y = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()

        if self.x in range(532, 748) and self.y in range(422, 480):
            if self.mouseleft:
                mainmenuflag = False
                heroselectionflag = True
            if AdminPage.adminflag:
                self.screen.blit(self.background7startadmin, (0, 0))
            else:
                self.screen.blit(self.backgroundstart, (0, 0))
        if self.x in range(450, 829) and self.y in range(517, 575):
            if self.mouseleft:
                options = True
                mainmenuflag = False
            if AdminPage.adminflag:
                self.screen.blit(self.background7optionsadmin, (0, 0))
            else:
                self.screen.blit(self.backgroundoptions, (0, 0))
            pass

        if self.x in range(560, 720) and self.y in range(618, 685):
            if AdminPage.adminflag:
                self.screen.blit(self.background7exitadmin, (0, 0))
            else:
                self.screen.blit(self.backgroundexit, (0, 0))
            if self.mouseleft:
                quit()

        if self.x in range(24, 183) and self.y in range(656, 684):
            if self.mouseleft:
                LoginRegister.loginflag = True
                mainmenuflag = False

        if self.x in range(35, 332) and self.y in range(46, 78):
            if self.mouseleft:
                leaderboardflag = True
                mainmenuflag = False

        if self.x in range(970, 1241) and self.y in range(630, 669):
            if self.mouseleft:
                adminpageflag = True
                mainmenuflag = False

    def start_game(self):
        global gameflag, swordsmanskillsflag, elfskillsflag, darkmageskillsflag, demonhunterskillsflag, heroselectionflag, swordsmaninfoflag, elfinfoflag, darkmageinfoflag, demonhunterinfoflag
        self.mx, self.my = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()
        if self.mx in range(902, 1193) and self.my in range(657, 685):
            if self.mouseleft:
                Game.game = True
                swordsmanskillsflag = False
                elfskillsflag = False
                darkmageskillsflag = False
                demonhunterskillsflag = False
                heroselectionflag = False
                swordsmaninfoflag = False
                elfinfoflag = False
                darkmageinfoflag = False
                demonhunterinfoflag = False

    def options_render(self):
        global volume, options, mainmenuflag, counter
        self.keys = pygame.key.get_pressed()
        self.font = pygame.font.Font('font/BALLOON DREAMS.ttf',20)
        self.x, self.y = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()
        self.volumeon = self.font.render("ON", True, (255, 255, 255))
        self.volumeoff = self.font.render("OFF", True, (255, 255, 255))
        self.screen.blit(self.option, (0, 0))
        if volume:
            self.screen.blit(self.volumeon, (340, 345))
        else:
            self.screen.blit(self.volumeoff, (335, 345))

        if self.x in range(340, 370) and self.y in range(352, 370):
            if self.mouseleft:
                if volume:
                    volume = False
                    counter = 0
                else:
                    volume = True

        if self.keys[pygame.K_ESCAPE]:
            options = False
            mainmenuflag = True


    def get_event(self, event):
        self.e = event
        self.admin = AdminPage.Admin(self.e)


    def MainMenu_Logic(self):
        global mainmenuflag, gameflag, nb, leaderboardflag, adminpageflag, options, counter

        self.keys = pygame.key.get_pressed()

        if volume and counter < 1:
            counter += 1
            MainMenuMusic()
        elif not volume:
            mixer.quit()

        if GameLoading.firstloadingflag and not LoginRegister.loginflag and not LoginRegister.registerflag:
            GameLoading.firstloading_bar_render()

        if adminpageflag:
            self.admin.AdminPageRender()
            if self.keys[pygame.K_ESCAPE]:
                adminpageflag = False
                mainmenuflag = True

        if leaderboardflag:
            Leaderboards.Leaderboard()
            ranks.Ranks_Logic()
            if self.keys[pygame.K_ESCAPE]:
                leaderboardflag = False
                mainmenuflag = True

        if LoginRegister.loginflag == False and LoginRegister.registerflag == False and \
                leaderboardflag == False and adminpageflag == False and heroselectionflag == False\
                and swordsmaninfoflag == False and swordsmanskillsflag == False and Game.game == False and not options and GameLoading.firstloadingflag == False and mainmenuflag == False:
            mainmenuflag = True

        if LoginRegister.loginflag == True or LoginRegister.registerflag == True:
            pass

        elif mainmenuflag:
            self.mainmenu_render()
            self.mainmenu_select()
            self.mainmenu_render()
            self.mainmenu_select()
            ClickingSound()

        elif heroselectionflag:
            self.hero_selection()
            ClickingSound()

        elif swordsmaninfoflag:
            self.swordsman_info_render()
            self.start_goback()
            ClickingSound()

        elif elfinfoflag:
            self.elf_info_render()
            self.start_goback()
            ClickingSound()

        elif darkmageinfoflag:
            self.darkmage_info_render()
            self.start_goback()
            ClickingSound()

        elif demonhunterinfoflag:
            self.demonhunter_info_render()
            self.start_goback()
            ClickingSound()

        elif demonhunterskillsflag:
            self.demonhunter_skills_render()
            self.start_goback()
            self.start_game()
            ClickingSound()

        elif swordsmanskillsflag:
            self.swordsman_skills_render()
            self.start_goback()
            self.start_game()
            ClickingSound()

        elif elfskillsflag:
            self.elf_skills_render()
            self.start_goback()
            self.start_game()
            ClickingSound()


        elif darkmageskillsflag:
            self.darkmage_skills_render()
            self.start_goback()
            self.start_game()
            ClickingSound()

        elif options:
            self.options_render()
            ClickingSound()

        elif Game.game:
            mixer.quit()
            self.Game_Run.Game_Main()



