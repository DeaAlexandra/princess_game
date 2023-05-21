import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))
taustakuva = pygame.image.load("castle_background.png")
puu = pygame.image.load("tree.png")
lattia = pygame.image.load("stone_floor_wide.png")
robo = pygame.image.load("princess_1.png")
ovi = pygame.image.load("gate.png")
sx, sy = naytto.get_size()
x = 100
y = sy - robo.get_height() - 15
nopeus = 2
oikealle = False
vasemmalle = False
suunta = 0
ylos = False
alas = False


# Vihreä väri RGB-arvoina
vihrea = (70, 90, 65)

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                suunta = 1
            if tapahtuma.key == pygame.K_RIGHT:
                suunta = 2

        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                suunta = 0
            if tapahtuma.key == pygame.K_RIGHT:
                suunta = 0

        if tapahtuma.type == pygame.QUIT:
            exit()

    if suunta == 2:
        x += nopeus
        if x >= sx - robo.get_width() - ovi.get_width() // 2:
            x = 0 + ovi.get_width() // 2
    if suunta == 1 and x >= 0 + ovi.get_width() // 2:
        x -= nopeus
        if x <= 0 + ovi.get_width() // 2:
            x = sx - robo.get_width() - ovi.get_width() // 2


    naytto.fill((139, 178, 217))

    # Piirrä linna 
    naytto.blit(taustakuva, (sx / 2 - taustakuva.get_width() / 2, sy - taustakuva.get_height()))
    
    naytto.blit(puu, (0 - puu.get_width() / 2, sy - puu.get_height() - 10))
    naytto.blit(puu, (sx - puu.get_width() / 2 - 15, sy - puu.get_height() - 10))
    naytto.blit(lattia, (0, sy - lattia.get_height() + 18))

    naytto.blit(robo, (x, y))
    naytto.blit(ovi, (0, 480 - ovi.get_height() - 10))
    naytto.blit(ovi, (sx - ovi.get_width(), sy - ovi.get_height() - 10))
    pygame.display.flip()

    kello.tick(60)

pygame.quit()
