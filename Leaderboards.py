import Database
import pygame
import LoginRegister

screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
leaderboardsacc = {}


def Leaderboard():
    leaderboard = pygame.image.load('photos/leaderboards2.png')
    leaderboard = pygame.transform.scale(leaderboard, (1280, 720))
    screen.blit(leaderboard, (0, 0))
    counter = 0
    bronze = pygame.image.load('ranks/Bronze.png')
    bronze = pygame.transform.scale(bronze, (50, 40))
    silver = pygame.image.load('ranks/Silver.png')
    silver = pygame.transform.scale(silver, (50, 40))
    ruby = pygame.image.load('ranks/Ruby.png')
    ruby = pygame.transform.scale(ruby, (50, 40))
    imperial = pygame.image.load('ranks/Imperial.png')
    imperial = pygame.transform.scale(imperial, (50, 40))
    legend = pygame.image.load('ranks/Legend.png')
    legend = pygame.transform.scale(legend, (50, 40))
    champion = pygame.image.load('ranks/Champion.png')
    champion = pygame.transform.scale(champion, (50, 40))

    for x in range(0, len(Database.nicknames)):
        leaderboardsacc.update({Database.nicknames[counter]: Database.playerpoints[counter]})
        counter += 1
    leaderboardsacc_sorted = sorted(leaderboardsacc.items(), key=lambda x: x[1], reverse=True)

    font = pygame.font.Font('font/BALLOON DREAMS.ttf', 18)
    px, py = 450, 180
    counter2 = 0
    for x in range(0, len(leaderboardsacc_sorted)):
        if counter2 == 7:
            break
        p = leaderboardsacc_sorted[x]
        n = p[0]
        pp = p[1]
        nicknametext = font.render(n, True, (255, 255, 255))
        pointstext = font.render(str(pp), True, (255, 255, 255))
        if p[0] == LoginRegister.loggedinnickname:
            currentplace = font.render(f'Your current place: {x + 1}', True, (255, 255, 255))
            screen.blit(currentplace, (490, 100))
        if p[1] >= 10000:
            screen.blit(nicknametext, (px, py))
            screen.blit(pointstext, (795, py))
        elif p[1] >= 1000:
            screen.blit(nicknametext, (px, py))
            screen.blit(pointstext, (807, py))
        elif p[1] >= 100:
            screen.blit(nicknametext, (px, py))
            screen.blit(pointstext, (810, py))
        else:
            screen.blit(nicknametext, (px, py))
            screen.blit(pointstext, (840, py))

        if p[1] >= 0 and p[1] <= 500:
            screen.blit(bronze, (855, py - 7))

        if p[1] > 500 and p[1] <= 700:
            screen.blit(silver, (855, py - 7))

        if p[1] > 700 and p[1] <= 1000:
            screen.blit(ruby, (855, py - 7))

        if p[1] > 1000 and p[1] <= 1300:
            screen.blit(imperial, (855, py - 7))

        if p[1] > 1300 and p[1] <= 2000:
            screen.blit(legend, (855, py - 7))

        if p[1] > 2000:
            screen.blit(champion, (855, py - 7))

        counter2 += 1
        if counter2 < 4:
            py += 78
        else:
            py += 60



Leaderboard()













