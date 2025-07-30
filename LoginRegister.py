import pygame
import Database
import tkinter as tk
import AdminPage


root = tk.Tk()


registerflag = False

register_email = 'Click here for input'
register_nickname = 'Click here for input'
register_password = 'Click here for input'
register_confirmpassword = 'Click here for input'

register_emailflag = False
register_nicknameflag = False
register_passwordflag = False
register_confirmpasswordflag = False

loginflag = True
email = 'Click here for input'
password = 'Click here for input'
emailflag = False
passwordflag = False

loggedinnickname = ''
loggedinpoints = 0
loggedinbanduration = 0

emailde = False
passnc = False
banflag = False


class Login:
    def __init__(self, screen):
        self.registerpage = pygame.image.load('photos/registerpage.jpg')
        self.registerpage = pygame.transform.scale(self.registerpage, (1280, 720))
        self.loginpage = pygame.image.load('photos/loginpage.jpg')
        self.loginpage = pygame.transform.scale(self.loginpage,(1280, 720))
        self.screen = screen
        self.font = pygame.font.Font('font/BALLOON DREAMS.ttf', 13)

    def register_functions(self):
        global loginflag, registerflag, register_email, register_emailflag, register_password, register_passwordflag, register_nickname, register_nicknameflag, register_confirmpassword, register_confirmpasswordflag
        self.x, self.y = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()
        if self.x in range(559, 743) and self.y in range(344, 362):

            if self.mouseleft:
                if register_email == 'Click here for input':
                    register_email = ''
                else:
                    register_email = register_email
                register_emailflag = True
                register_passwordflag = False
                register_password = register_password
                register_nicknameflag = False
                register_nickname = register_nickname
                register_confirmpasswordflag = False
                register_confirmpassword = register_confirmpassword

        if self.x in range(606, 782) and self.y in range(390, 404):
            if self.mouseleft:
                if register_nickname == 'Click here for input':
                    register_nickname = ''
                else:
                    register_nickname = register_nickname
                register_emailflag = False
                register_email = register_email
                register_passwordflag = False
                register_password = register_password
                register_nicknameflag = True
                register_confirmpasswordflag = False
                register_confirmpassword = register_confirmpassword

        if self.x in range(609, 784) and self.y in range(436, 452):
            if self.mouseleft:
                if register_password == 'Click here for input':
                    register_password = ''
                else:
                    register_password = register_password
                register_emailflag = False
                register_email = register_email
                register_passwordflag = True
                register_nicknameflag = False
                register_nickname = register_nickname
                register_confirmpasswordflag = False
                register_confirmpassword = register_confirmpassword

        if self.x in range(715, 888) and self.y in range(483, 496):
            if self.mouseleft:
                if register_confirmpassword == 'Click here for input':
                    register_confirmpassword = ''
                else:
                    register_confirmpassword = register_confirmpassword
                register_emailflag = False
                register_email = register_email
                register_passwordflag = False
                register_password = register_password
                register_nicknameflag = False
                register_nickname = register_nickname
                register_confirmpasswordflag = True

        if self.event.type == pygame.KEYDOWN and register_emailflag:
            if self.event.key == pygame.K_BACKSPACE:
                register_email = register_email[:-1]
            else:
                if len(register_email) < 25:
                    register_email += self.event.unicode

        if self.event.type == pygame.KEYDOWN and register_nicknameflag:
            if self.event.key == pygame.K_BACKSPACE:
                register_nickname = register_nickname[:-1]
            else:
                if len(register_nickname) < 25:
                    register_nickname += self.event.unicode

        if self.event.type == pygame.KEYDOWN and register_passwordflag:
            if self.event.key == pygame.K_BACKSPACE:
                register_password = register_password[:-1]
            else:
                if len(register_password) < 25:
                    register_password += self.event.unicode

        if self.event.type == pygame.KEYDOWN and register_confirmpasswordflag:
            if self.event.key == pygame.K_BACKSPACE:
                register_confirmpassword = register_confirmpassword[:-1]
            else:
                if len(register_confirmpassword) < 25:
                    register_confirmpassword += self.event.unicode

        if self.x in range(565, 711) and self.y in range(540, 580):
            if self.mouseleft:
                Database.registermethod(register_email, register_nickname, register_password, register_confirmpassword)
                if Database.registervalid:
                    registerflag = False

    def register_render(self):
        self.email_surface = self.font.render(register_email, True, (255, 255, 255))
        self.nickname_surface = self.font.render(register_nickname, True, (255, 255, 255))
        self.password_surface = self.font.render(register_password, True, (255, 255, 255))
        self.confirm_password_surface = self.font.render(register_confirmpassword, True, (255, 255, 255))
        self.screen.blit(self.registerpage, (0, 0))
        self.screen.blit(self.email_surface, (562, 342))
        self.screen.blit(self.nickname_surface,(610, 386))
        self.screen.blit(self.password_surface, (613, 432))
        self.screen.blit(self.confirm_password_surface, (719, 478))

    def ban(self):
        self.ban_text = self.font.render(f'Your account has been banned: {loggedinbanduration} hours({loggedinbanduration/24} days)', True, (255, 50, 0))
        self.screen.blit(self.ban_text,(450, 560))

    def login_functions(self):
        global loginflag, registerflag, email, emailflag, password, passwordflag, loggedinpoints, loggedinnickname, loggedinbanduration, banflag, emailde, passnc
        self.x, self.y = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()

        if self.x in range (551, 755) and self.y in range(387, 404):
            if self.mouseleft:
                if email == 'Click here for input':
                    email = ''
                else:
                    email = email
                emailflag = True
                passwordflag = False
                password = password

        if self.x in range (605, 805) and self.y in range(442, 459):
            if self.mouseleft:
                if password == 'Click here for input':
                    password = ''
                else:
                    password = password
                passwordflag = True
                emailflag = False
                email = email

        if self.event.type == pygame.KEYDOWN and emailflag:
            if self.event.key == pygame.K_BACKSPACE:
                email = email[:-1]
            else:
                if len(email) < 25:
                    email += self.event.unicode

        if self.event.type == pygame.KEYDOWN and passwordflag:
            if self.event.key == pygame.K_BACKSPACE:
                password = password[:-1]
            else:
                if len(password) < 25:
                    password += self.event.unicode

        if self.x in range(579, 701) and self.y in range(511, 548):
            if self.mouseleft:
                self.id = 0
                banflag = False
                if email in Database.emails:
                    emailde = False
                    for x in Database.emails:
                        if x == email:
                            if Database.passwords[self.id] == password:
                                loggedinnickname = Database.nicknames[self.id]
                                loggedinpoints = Database.playerpoints[self.id]
                                loggedinbanduration = Database.banduration[self.id]
                                if loggedinbanduration > 0:
                                    banflag = True
                                    passnc = False
                                    emailde = False
                                else:
                                    loginflag = False
                                    passnc = False
                                    emailde = False
                                    if loggedinnickname == "Admin":
                                        AdminPage.adminflag = True
                                    else:
                                        AdminPage.adminflag = False
                            else:
                                passnc = True
                        else:
                            self.id += 1
                else:
                    emailde = True


    def login_errors(self):
        global emailde, passnc
        self.email_d_exist = self.font.render('There is no accounts linked to that email', True, (255, 210, 240))
        self.password_d_match = self.font.render('Incorrect password', True, (255, 210, 240))
        if emailde:
            self.screen.blit(self.email_d_exist,(462, 560))
        elif passnc:
            self.screen.blit(self.password_d_match,(555, 560))

    def login_page_render(self):
        global email
        self.email_surface = self.font.render(email, True, (255, 255, 255))
        self.password_surface = self.font.render(password, True, (255, 255, 255))
        self.screen.blit(self.loginpage,(0, 0))
        self.screen.blit(self.email_surface, (560, 387))
        self.screen.blit(self.password_surface, (610, 441))

    def login_or_register_switch(self):
        global loginflag, registerflag
        self.x, self.y = pygame.mouse.get_pos()
        self.mouseleft, self.mousemiddle, self.mouseright = pygame.mouse.get_pressed()

        if self.x in range(507, 771) and self.y in range(607, 632):
            if self.mouseleft:
                if registerflag:
                    registerflag = False
                    loginflag = True
                elif loginflag:
                    registerflag = True
                    loginflag = False

    def login_register_logic(self, event):
        self.event = event
        self.login_or_register_switch()
        if loginflag:
            self.login_page_render()
            self.login_functions()
            self.login_errors()
            if banflag:
                self.ban()
        if registerflag:
            self.register_render()
            self.register_functions()
            Database.register_errors_render()








