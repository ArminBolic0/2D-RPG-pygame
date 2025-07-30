import mysql.connector
import pygame
import re

pygame.init()

connection = mysql.connector.connect(host = 'localhost',
                                     database = 'heroquestaccounts',
                                     user = 'root',
                                     password = 'root')

mycursor = connection.cursor()

mycursor.execute("SELECT * from accounts")

screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

font = pygame.font.Font('font/BALLOON DREAMS.ttf', 13)

ids = []
emails = []
nicknames = []
passwords = []
playerpoints = []
banduration = []

emailinvalid = False
emailtaken = False
nicknametaken = False
passdm = False
fillblank = False


counter = 0

registervalid = False

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def registermethod(emailarg, nicknamearg, passwordarg, cpasswordarg):
    global registervalid, emailtaken, nicknametaken, passdm, counter, emailinvalid, fillblank
    email = emailarg
    nickname = nicknamearg
    password = passwordarg
    cpassword = cpasswordarg

    if len(email) > 0 and len(nickname) > 0 and len(
            password) > 0 and email != 'Click here for input' and nickname != 'Click here for input' and password != 'Click here for input':
        fillblank = False
        if (re.search(regex, email)):
            emailinvalid = False
            if email in emails:
                    emailinvalid = False
                    emailtaken = True

            elif nickname in nicknames:
                emailinvalid = False
                emailtaken = False
                nicknametaken = True

            elif password != cpassword:
                emailinvalid = False
                emailtaken = False
                nicknametaken = False
                passdm = True
            else:
                emailinvalid = False
                emailtaken = False
                nicknametaken = False
                passdm = False
                mycursor.execute("INSERT INTO accounts (Email, Nickname, Passw, Points, banduration) VALUES (%s, %s, %s, %s, %s)", (email, nickname, password, 0, 0))
                connection.commit()
                registervalid = True
                for x in mycursor:
                    for y in x:
                        if counter == 0:
                            counter += 1
                        elif counter == 1:
                            emails.append(y)
                            counter += 1
                        elif counter == 2:
                            nicknames.append(y)
                            counter += 1
                        elif counter == 3:
                            passwords.append(y)
                            counter += 1
                        elif counter == 4:
                            playerpoints.append(y)
                            counter = 0
        else:
            emailinvalid = True
            passdm = False
            emailtaken = False
            nicknametaken = False
    else:
        fillblank = True

def register_errors_render():
    global emailtaken, nicknametaken, passdm, fillblank, emailinvalid
    emailtakentext = font.render('Email already exists', True, (255, 255, 255))
    nicknametakentext = font.render('Nickname already taken', True, (255, 255, 255))
    passdmtext = font.render('Password doesnt match', True, (255, 255, 255))
    emailinvalidtext = font.render('Invalid email', True, (255, 100, 0))
    fillblanktext = font.render('You have to fill in all the requirements.', True, (255, 200, 100))
    if fillblank:
        screen.blit(fillblanktext, (470, 508))
    elif emailinvalid:
        screen.blit(emailinvalidtext, (585, 508))
    elif emailtaken:
        screen.blit(emailtakentext,(550, 508))
    elif nicknametaken:
        screen.blit(nicknametakentext,(550, 508))
    elif passdm:
        screen.blit(passdmtext, (545, 508))


for x in mycursor:
    for y in x:
        if counter == 0:
            ids.append(y)
            counter += 1
        elif counter == 1:
            emails.append(y)
            counter += 1
        elif counter == 2:
            nicknames.append(y)
            counter += 1
        elif counter == 3:
            passwords.append(y)
            counter += 1
        elif counter == 4:
            playerpoints.append(y)
            counter += 1
        elif counter == 5:
            banduration.append(y)
            counter = 0



