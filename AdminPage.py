import pygame
import Database

screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
adminflag = False
banwindowflag = False
deletewindowflag = False
banidflag = False
bandurationflag = False
deleteidflag = False

playerid = "0"
banduration = "0"


class Admin:
    def __init__(self, events):
        self.adminpage = pygame.image.load('photos/adminpage.png')
        self.adminpage = pygame.transform.scale(self.adminpage, (1280, 720))
        self.banwindow = pygame.image.load('photos/banwindow.png')
        self.banwindow = pygame.transform.scale(self.banwindow, (800, 400))
        self.deletewindow = pygame.image.load('photos/deletewindow.png')
        self.deletewindow = pygame.transform.scale(self.deletewindow, (800, 400))
        self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 14)
        self.fontban = pygame.font.Font('font/BALLOON DREAMS.ttf', 25)
        self.idx, self.nnx, self.banx = 100, 290, 515
        self.mx, self.my = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()
        self.e = events
        self.y = 270

    def AdminPageRender(self):
        global playerid, banduration, banwindowflag, deletewindowflag, banidflag, bandurationflag, deleteidflag
        self.bantext = self.fontban.render(str(playerid), True, (173, 72, 9))
        self.bantextd = self.fontban.render(str(banduration), True, (173, 72, 9))
        self.deletetext = self.fontban.render(str(playerid), True, (173, 72, 9))
        self.keys = pygame.key.get_pressed()
        print(self.mx, self.my)
        screen.blit(self.adminpage, (0, 0))

        if self.mx in range(900, 1014) and self.my in range(358, 389):
            if self.mouseleft:
                banwindowflag = True
                deletewindowflag = False

        if self.mx in range(727, 1187) and self.my in range(498, 529):
            if self.mouseleft:
                deletewindowflag = True
                banwindowflag = False

        for x in range(0, len(Database.nicknames)):
            id = Database.ids[x]
            nn = Database.nicknames[x]
            ban = Database.banduration[x]
            if nn != "Admin":
                idtext = self.font.render(str(id), True, (255, 255, 255))
                nicknametext = self.font.render(nn, True, (255, 255, 255))
                bantext = self.font.render(f'{ban} hours', True, (255, 255, 255))
                screen.blit(idtext, (self.idx, self.y))
                screen.blit(nicknametext, (self.nnx, self.y))
                screen.blit(bantext, (self.banx, self.y))
                self.y += 20

        if banwindowflag:
            screen.blit(self.banwindow, (200, 200))
            screen.blit(self.bantext,(515, 361))
            screen.blit(self.bantextd, ( 820, 458))
            if self.keys[pygame.K_ESCAPE]:
                Database.mycursor.execute("SELECT * from accounts")
                Database.ids = []
                Database.emails = []
                Database.nicknames = []
                Database.passwords = []
                Database.playerpoints = []
                Database.banduration = []
                counter = 0
                for x in Database.mycursor:
                    for y in x:
                        if counter == 0:
                            Database.ids.append(y)
                            counter += 1
                        elif counter == 1:
                            Database.emails.append(y)
                            counter += 1
                        elif counter == 2:
                            Database.nicknames.append(y)
                            counter += 1
                        elif counter == 3:
                            Database.passwords.append(y)
                            counter += 1
                        elif counter == 4:
                            Database.playerpoints.append(y)
                            counter += 1
                        elif counter == 5:
                            Database.banduration.append(y)
                            counter = 0

                for x in range(0, len(Database.nicknames)):
                    id = Database.ids[x]
                    nn = Database.nicknames[x]
                    ban = Database.banduration[x]
                    if nn != "Admin":
                        idtext = self.font.render(str(id), True, (255, 255, 255))
                        nicknametext = self.font.render(nn, True, (255, 255, 255))
                        bantext = self.font.render(f'{ban} hours', True, (255, 255, 255))
                        screen.blit(idtext, (self.idx, self.y))
                        screen.blit(nicknametext, (self.nnx, self.y))
                        screen.blit(bantext, (self.banx, self.y))
                        self.y += 20
                banwindowflag = False

            if self.mx in range(508, 532) and self.my in range(372, 401):
                if self.mouseleft:
                    banidflag = True
                    bandurationflag = False

            if self.mx in range(813, 837) and self.my in range(467, 497):
                if self.mouseleft:
                    bandurationflag = True
                    banidflag = False

            if self.mx in range(465, 729) and self.my in range(547, 579):
                if self.mouseleft:
                    if int(playerid) in Database.ids:
                        if int(banduration) > 0:
                            Database.mycursor.execute(f"UPDATE accounts SET banduration = {int(banduration)} where id = {int(playerid)}")
                            Database.connection.commit()
                            Database.mycursor.execute("SELECT * from accounts")
                            Database.ids = []
                            Database.emails = []
                            Database.nicknames = []
                            Database.passwords = []
                            Database.playerpoints = []
                            Database.banduration = []
                            counter = 0
                            for x in Database.mycursor:
                                for y in x:
                                    if counter == 0:
                                        Database.ids.append(y)
                                        counter += 1
                                    elif counter == 1:
                                        Database.emails.append(y)
                                        counter += 1
                                    elif counter == 2:
                                        Database.nicknames.append(y)
                                        counter += 1
                                    elif counter == 3:
                                        Database.passwords.append(y)
                                        counter += 1
                                    elif counter == 4:
                                        Database.playerpoints.append(y)
                                        counter += 1
                                    elif counter == 5:
                                        Database.banduration.append(y)
                                        counter = 0

                            for x in range(0, len(Database.nicknames)):
                                id = Database.ids[x]
                                nn = Database.nicknames[x]
                                ban = Database.banduration[x]
                                if nn != "Admin":
                                    idtext = self.font.render(str(id), True, (255, 255, 255))
                                    nicknametext = self.font.render(nn, True, (255, 255, 255))
                                    bantext = self.font.render(f'{ban} hours', True, (255, 255, 255))
                                    screen.blit(idtext, (self.idx, self.y))
                                    screen.blit(nicknametext, (self.nnx, self.y))
                                    screen.blit(bantext, (self.banx, self.y))
                                    self.y += 20
                            banwindowflag = False
                        else:
                            print("ovdje nešto ne radi")
                    else:
                        print("Ne radi")

            if self.e.type == pygame.KEYDOWN and banidflag:
                if self.e.key == pygame.K_BACKSPACE:
                    playerid = playerid[:-1]
                elif self.e.key == pygame.K_0 or self.e.key == pygame.K_1 or self.e.key == pygame.K_2 or self.e.key == pygame.K_3 or self.e.key == pygame.K_4 or self.e.key == pygame.K_5 or self.e.key == pygame.K_6 or self.e.key == pygame.K_7 or self.e.key == pygame.K_8 or self.e.key == pygame.K_9:
                    if len(playerid) < 10:
                        playerid += self.e.unicode
                else:
                    pass

            if self.e.type == pygame.KEYDOWN and bandurationflag:
                if self.e.key == pygame.K_BACKSPACE:
                    banduration = banduration[:-1]
                elif self.e.key == pygame.K_0 or self.e.key == pygame.K_1 or self.e.key == pygame.K_2 or self.e.key == pygame.K_3 or self.e.key == pygame.K_4 or self.e.key == pygame.K_5 or self.e.key == pygame.K_6 or self.e.key == pygame.K_7 or self.e.key == pygame.K_8 or self.e.key == pygame.K_9:
                    if len(banduration) < 10:
                        banduration += self.e.unicode
                else:
                    pass

        if deletewindowflag:
            screen.blit(self.deletewindow, (200, 200))
            screen.blit(self.deletetext, (680, 385))

            if self.keys[pygame.K_ESCAPE]:
                Database.mycursor.execute("SELECT * from accounts")
                Database.ids = []
                Database.emails = []
                Database.nicknames = []
                Database.passwords = []
                Database.playerpoints = []
                Database.banduration = []
                counter = 0
                self.y = 0
                for x in Database.mycursor:
                    for y in x:
                        if counter == 0:
                            Database.ids.append(y)
                            counter += 1
                        elif counter == 1:
                            Database.emails.append(y)
                            counter += 1
                        elif counter == 2:
                            Database.nicknames.append(y)
                            counter += 1
                        elif counter == 3:
                            Database.passwords.append(y)
                            counter += 1
                        elif counter == 4:
                            Database.playerpoints.append(y)
                            counter += 1
                        elif counter == 5:
                            Database.banduration.append(y)
                            counter = 0

                for x in range(0, len(Database.nicknames)):
                    id = Database.ids[x]
                    nn = Database.nicknames[x]
                    ban = Database.banduration[x]
                    if nn != "Admin":
                        idtext = self.font.render(str(id), True, (255, 255, 255))
                        nicknametext = self.font.render(nn, True, (255, 255, 255))
                        bantext = self.font.render(f'{ban} hours', True, (255, 255, 255))
                        screen.blit(idtext, (self.idx, self.y))
                        screen.blit(nicknametext, (self.nnx, self.y))
                        screen.blit(bantext, (self.banx, self.y))
                        self.y += 20
                deletewindowflag = False

            if self.mx in range(675, 904) and self.my in range(385, 423):
                if self.mouseleft:
                    deleteidflag = True

            if self.e.type == pygame.KEYDOWN and deleteidflag:
                if self.e.key == pygame.K_BACKSPACE:
                    playerid = playerid[:-1]
                elif self.e.key == pygame.K_0 or self.e.key == pygame.K_1 or self.e.key == pygame.K_2 \
                        or self.e.key == pygame.K_3 or self.e.key == pygame.K_4 or self.e.key == pygame.K_5 \
                        or self.e.key == pygame.K_6 or self.e.key == pygame.K_7 or self.e.key == pygame.K_8 or self.e.key == pygame.K_9:
                    if len(playerid) < 10:
                        playerid += self.e.unicode
                else:
                    pass

            if self.mx in range(405, 797) and self.my in range(535, 582):
                if self.mouseleft:
                    if int(playerid) in Database.ids:
                        Database.mycursor.execute(f"DELETE FROM accounts WHERE id = {int(playerid)}")
                        Database.connection.commit()
                        Database.mycursor.execute("SELECT * from accounts")
                        Database.ids = []
                        Database.emails = []
                        Database.nicknames = []
                        Database.passwords = []
                        Database.playerpoints = []
                        Database.banduration = []
                        counter = 0
                        for x in Database.mycursor:
                            for y in x:
                                if counter == 0:
                                    Database.ids.append(y)
                                    counter += 1
                                elif counter == 1:
                                    Database.emails.append(y)
                                    counter += 1
                                elif counter == 2:
                                    Database.nicknames.append(y)
                                    counter += 1
                                elif counter == 3:
                                    Database.passwords.append(y)
                                    counter += 1
                                elif counter == 4:
                                    Database.playerpoints.append(y)
                                    counter += 1
                                elif counter == 5:
                                    Database.banduration.append(y)
                                    counter = 0

                        for x in range(0, len(Database.nicknames)):
                            id = Database.ids[x]
                            nn = Database.nicknames[x]
                            ban = Database.banduration[x]
                            if nn != "Admin":
                                idtext = self.font.render(str(id), True, (255, 255, 255))
                                nicknametext = self.font.render(nn, True, (255, 255, 255))
                                bantext = self.font.render(f'{ban} hours', True, (255, 255, 255))
                                screen.blit(idtext, (self.idx, self.y))
                                screen.blit(nicknametext, (self.nnx, self.y))
                                screen.blit(bantext, (self.banx, self.y))
                                self.y += 20
                        deletewindowflag = False