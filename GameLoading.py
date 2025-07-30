import pygame
import Game

gameloadingbackground = pygame.image.load('photos/gameloading.jpg')
gameloadingbackground = pygame.transform.scale(gameloadingbackground, (1280, 720))
firstgameloadingbackground = pygame.image.load('photos/firstgameloading.jpg')
firstgameloadingbackground = pygame.transform.scale(firstgameloadingbackground, (1280, 720))

screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

loadingflag = True
firstloadingflag = True
loading = 0

def loading_bar_render():
    global loadingflag, loading
    Game.gameeventflag = True
    maximum_loading = 100
    loading_bar_lenght = 600
    loading_ratio = maximum_loading / loading_bar_lenght
    currentloading = loading
    font = pygame.font.Font('font/Decay-M5RB.ttf', 28)
    font2 = pygame.font.Font('font/BALLOON DREAMS.ttf', 20)
    loadingtext = font.render("LOADING", True, (255, 255, 255))
    loadingperctext = font2.render(f'{int(loading)}%', True, (13, 191, 85))
    if loadingflag:
        screen.blit(gameloadingbackground,(0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (350, 350, int(currentloading / loading_ratio), 40))
        pygame.draw.rect(screen, (255, 255, 255), (350, 350, loading_bar_lenght, 40), 4)
        screen.blit(loadingperctext, (635, 350))
        screen.blit(loadingtext, (540, 300))
        if loading >= 0:
            loading += 0.4
        if loading >= 100:
            loadingflag = False
            loading = 0

def firstloading_bar_render():
    global firstloadingflag, loading
    Game.gameeventflag = True
    maximum_loading = 100
    loading_bar_lenght = 600
    loading_ratio = maximum_loading / loading_bar_lenght
    currentloading = loading
    font = pygame.font.Font('font/Decay-M5RB.ttf', 28)
    font2 = pygame.font.Font('font/BALLOON DREAMS.ttf', 20)
    loadingtext = font.render("LOADING", True, (255, 255, 255))
    loadingperctext = font2.render(f'{int(loading)}%', True, (13, 191, 85))
    if firstloadingflag:
        screen.blit(firstgameloadingbackground,(0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (350, 350, int(currentloading / loading_ratio), 40))
        pygame.draw.rect(screen, (255, 255, 255), (350, 350, loading_bar_lenght, 40), 4)
        screen.blit(loadingperctext, (635, 350))
        screen.blit(loadingtext, (540, 300))
        if loading >= 0:
            loading += 0.4
        if loading >= 100:
            firstloadingflag = False
            loading = 0
            Game.gameeventflag = False
