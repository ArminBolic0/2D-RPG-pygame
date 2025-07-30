from pygame import mixer
import pygame
import MainMenu

def MainMenuMusic():
    mixer.init()
    mainmenumusic = pygame.mixer.Sound('sound/mainmenumusic.mp3')
    if MainMenu.volume:
        mainmenumusic.play(-1)
    else:
        mixer.quit()

def ClickingSound():
    mixer.init()
    click = pygame.mixer.Sound('sound/clicksound.mp3')
    click.set_volume(0.5)
    mouseleft, mousemiddle, mouseright = pygame.mouse.get_pressed()
    if mouseleft:
        click.play()



