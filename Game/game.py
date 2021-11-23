# 1 - library import bre
import math
import pygame
from pygame.locals import *

# 2 - install game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# mapping tombol
keys = {
    "atas": False,
    "bawah": False,
    "kiri": False,
    "kanan": False,
}

running = True

playerpos = [100, 100] # install posisi player
score = 0
arrows = [ ] # list untuk arrows

# 3 - mengambil asset game
# 3.1 - Mengambil asset foto
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")


## 4 - looping Game

while(running):

    # 5 - screen
    screen.fill(0)

    # 6 - gambar objek game
    ## gambar 1
    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass, (x*100, y*100))

        

    ## gambar kastil
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    
    # gambar player
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(mouse_position[1] - (playerpos[1]+32), mouse_position[0] - (playerpos[0]+26))
    player_rotation = pygame.transform.rotate(player, 360 - angle * 57.29)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width / 2, playerpos[1] - player_rotation.get_rect().height / 2)
    screen.blit (player_rotation, new_playerpos)

    # 6.1 - Gambar Peluru
    for bullet in arrows:
        arrow_index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[1])*10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet [1] > width or bullet[2] < -64 or bullet[2] > height :
            arrows.pop(arrow_index)
        arrow_index  += 1
        #gambar peluru
        for projectile in arrows :
            new_arrows = pygame.transform.rotate(arrows,360 - projectile[0]*57.29)
            screen.blit (new_arrows, projectile[1],projectile[2])

    # 7 - update screen
    pygame.display.flip()

    # 8 event looping
    for event in pygame.event.get():
        # event yang terjadi ketika tombol exit di klik
        if event.type == pygame.QUIT:
            pygame.Quit()
            exit(0)

        # event Tembak
        if event.type == pygame.MOUSEBUTTONDOWN:
            arrows.append([angle, new_playerpos[0]+32, new_playerpos[1]+32])

        # pengecekan keydown dan keyup
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys["atas"] = True
            elif event.key == K_a:
                keys["kiri"] = True
            elif event.key == K_d:
                keys["kanan"] = True
            elif event.key == K_s:
                keys["bawah"] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys["atas"] = False
            elif event.key == K_a:
                keys["kiri"] = False
            elif event.key == K_d:
                keys["kanan"] = False
            elif event.key == K_s:
                keys["bawah"] = False
    # - Berhenti Looping

    # 9 pergerakan player
    if keys["atas"]:
        playerpos[1] -= 5 # mengurangi nilai y
    elif keys["bawah"]:
        playerpos[1] += 5 # menambah nilai y
    elif keys["kiri"]:
        playerpos[0] -= 5 # mengurangi nilai x
    elif keys["kanan"]:
        playerpos[0] += 5 # Menambah nilai x
