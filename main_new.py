import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))
taustakuva = pygame.image.load("castle_background.png")
puu = pygame.image.load("tree.png")
lattia = pygame.image.load("stone_floor_wide.png")
princess = pygame.image.load("princess_1.png")
princess_large = pygame.image.load("princess_big.png")
portti = pygame.image.load("gate.png")
dragon = pygame.image.load("dragon.png")
arrow_left = pygame.image.load("arrow_left.png")
arrow_right = pygame.image.load("arrow_right.png")
start_button = pygame.image.load("start_button.png")
sx, sy = naytto.get_size()

y = sy - princess.get_height()
nopeus = 5
naytto.fill((139, 178, 217))


class Dragon:
    osui = False
    vaistetyt = 0
    def __init__(self):
        self.dragon = dragon
        self.x = random.randrange(portti.get_width(), sx - portti.get_width() - dragon.get_width())
        self.y = -(random.randrange(20, sy - dragon.get_height()))
        self.v = random.randrange(1, nopeus)
    def game_over(self):
        if Dragon.osui != True:
            self.y += self.v
    def osuma(self, princess_x, princess_y):
        if self.y > sy - princess.get_height() - dragon.get_height() + 10:
            if princess_x + princess.get_width() < self.x or princess_x > self.x + dragon.get_width():
                pass
            else:
                Dragon.osui = True



    def nollaa(self):
        self.x = random.randrange(portti.get_width(), sx - portti.get_width())
        self.y = -(random.randrange(20, sy - dragon.get_height()))
        self.v = random.randrange(1, 5)



class Peli:
    def __init__(self):
        pygame.init()
        #värit
        self.white = (255, 255, 255)
        self.white_transparent = (255, 255, 255, 128)
        self.green = (70, 90, 65)
        self.blue = (0, 0, 128)
        self.yellow = (175, 155, 125)
        self.dark_grey = (59, 56, 56)
        self.black = (0, 0, 0)

        pygame.display.set_caption('Väistä hirviötä')
        self.font = pygame.font.Font('bradley_hand_itc_tt_bold.ttf', 26)
        self.font_a = pygame.font.Font('bradley_hand_itc_tt_bold.ttf', 24)
        self.font_b = pygame.font.Font('bradley_hand_itc_tt_bold.ttf', 18)
        self.font_c = pygame.font.Font('bradley_hand_itc_tt_bold.ttf', 12)
        self.help = False
        self.suunta = 0
        self.princess_x = 100
        self.princess_y = 480 - princess.get_height()
        self.game_over = False
        self.help = False

        self.kello = pygame.time.Clock()
        naytto.fill((139, 178, 217))
        self.piirra_tausta()
        self.piirra_portti()
        self.aloitusikkuna()
        self.aloitusnapin_piirto()
        pygame.display.flip()




        self.silmukka()


    def silmukka(self):
        self.dragonlista = []
        for i in range(1,random.randrange(5,10)):
            self.dragonlista.append(Dragon())
        game_running = True
        napin_alue = pygame.Rect(360, 230, start_button.get_width(), start_button.get_height())
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    hiiren_x, hiiren_y = pygame.mouse.get_pos()
                    if napin_alue.collidepoint(hiiren_x, hiiren_y):
                        # Aloita peli
                        self.princess_x = sx // 2 - princess.get_width()
                        self.princess_y = sy - princess.get_height()
     
                        self.tutki_tapahtumat()



    def aloitusnapin_piirto(self):
        txtsurf_a = self.font.render("Aloita peli", True, self.dark_grey)
        naytto.blit(txtsurf_a, (320, 200))
        self.start_button = start_button
        naytto.blit(self.start_button, (360, 230))


    def aloitusikkuna(self):
       
        # Piirrä läpinäkyvä ikkuna tekstin alle
        ikkunan_koko = (sx - 40, sy - 40)
        ikkuna = pygame.Surface(ikkunan_koko, pygame.SRCALPHA)
        pygame.draw.rect(ikkuna, (255, 255, 255, 200), (0, 0, ikkunan_koko[0], ikkunan_koko[1]), border_radius=20)
        naytto.blit(ikkuna, (20, 20))

        txtsurf_b = self.font_a.render("Pelin tarkoituksena on", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 60))
        txtsurf_b = self.font_a.render("väistellä lohikäärmeitä ", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 90))
        txtsurf_b = self.font_a.render("joita laskeutuu taivaalta.", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 120))
        txtsurf_b = self.font_a.render("prinsessaa ohjataan", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 150))
        txtsurf_b = self.font_a.render("oikealle ja vasemmalle", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 180))
        self.arrow_left = arrow_left
        naytto.blit(self.arrow_left, (60, 210))
        self.arrow_right = arrow_right
        naytto.blit(self.arrow_right, (180, 210))
        txtsurf_b = self.font_a.render(" nuolinäppäimillä.", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 300))
        txtsurf_b = self.font_a.render("Voit siirtyä reunasta toiseen ", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 330))
        txtsurf_b = self.font_a.render("myös porttien kautta,", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 360))
        txtsurf_b = self.font_a.render("mutta varo lohikäärmeitä.", True, self.dark_grey)
        naytto.blit(txtsurf_b, (60, 390))
        txtsurf_c = self.font_c.render("Images by brgfx on Freepik", True, self.dark_grey)
        naytto.blit(txtsurf_c, (60, 440))       



        self.princess_large = princess_large
        xa = self.princess_x = sx - princess_large.get_width() - 30
        ya = self.princess_y = sy - princess_large.get_height() - 30
        naytto.blit(self.princess_large, (xa, ya))



    def tutki_tapahtumat(self):
        while True:

            for tapahtuma in pygame.event.get():

                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_LEFT:
                        self.suunta = 2
                    if tapahtuma.key == pygame.K_RIGHT:
                        self.suunta = 1
                if tapahtuma.type == pygame.KEYUP:
                    if tapahtuma.key == pygame.K_LEFT:
                        self.suunta = 0
                    if tapahtuma.key == pygame.K_RIGHT:
                        self.suunta = 0
                    if tapahtuma.key == pygame.K_SPACE:
                        self.suunta = 0
                        self.princess_x = sx // 2 - princess.get_width()
                        self.princess_y = sy - princess.get_height()
                        #kolikot
                        for k in self.dragonlista:
                            self.dragonlista = []
                            for i in range(1,random.randrange(5,10)):
                                self.dragonlista.append(Dragon())
                        Dragon.osui = False
                        Dragon.vaistetyt = 0
                    if tapahtuma.key == pygame.K_F1:
                        self.help = True
                    if tapahtuma.key == pygame.K_ESCAPE:
                       self.help = False
                if tapahtuma.type == pygame.QUIT:
                    exit()
            naytto.fill((139, 178, 217))
            self.piirra_tausta()
            self.piirra_portti()
            self.dragon_kasittely()


    def dragon_kasittely(self):
        #dragonin kasittely
        if self.help == False:
            for k in self.dragonlista:
                k.game_over()
                k.osuma(self.princess_x,self.princess_y)
                if k.y < 400:
                    naytto.blit(k.dragon, (k.x, k.y))
                else:
                    Dragon.vaistetyt += 1
                    print(Dragon.vaistetyt)
                    k.nollaa()
            if Dragon.osui == True:
                self.suunta = 0
            else:
                if self.suunta == 1:
                    self.princess_x += nopeus
                    if self.princess_x >= sx - princess.get_width() - portti.get_width() // 2:
                        self.princess_x = 0 + portti.get_width() // 2

                if self.suunta == 2 and self.princess_x >= 0 + portti.get_width() // 2:
                    self.princess_x -= nopeus
                    if self.princess_x <= 0 + portti.get_width() // 2:
                        self.princess_x = sx - princess.get_width() - portti.get_width() // 2
        self.princess = princess
        naytto.blit(self.princess, (self.princess_x, self.princess_y))
        # pisteet näytölle
        if Dragon.vaistetyt < 10:
            txtsurf = self.font.render(f"{Dragon.vaistetyt}", True, self.white)
            naytto.blit(txtsurf,(sx // 2 - 10, 210))

        else:
            txtsurf = self.font.render(f"{Dragon.vaistetyt}", True, self.white)
            naytto.blit(txtsurf,(sx // 2 - 15, 210))
        # pisteiden selite näytölle
        txtsurf = self.font_b.render(f"pisteet", True, self.white)
        naytto.blit(txtsurf,(sx // 2 - 25, 235))
        if Dragon.osui == True:
            txtsurf = self.font.render(f" Hävisit. Onnistuit väistämään {Dragon.vaistetyt} hirviötä", True, self.yellow, self.dark_grey)
            naytto.blit(txtsurf,(80,100))
        if self.help == True:
            self.aloitusikkuna()
            txtsurf = self.font.render("Paluu peliin = Esc", True, self.dark_grey)
            naytto.blit(txtsurf,(200,140))
        if self.help == False:
            txtsurf = self.font.render("Pause = F1,     Uusi peli = välilyönti", True, self.dark_grey)
            naytto.blit(txtsurf,(120,20))


        pygame.display.flip()
        self.kello.tick(60)

    def piirra_tausta(self):
            naytto.fill((139, 178, 217))
                        # kuusi vasen
            self.ylaoksa_v = [(0, 100), (50, 200), (0, 200)]
            self.keskioksa_v = [(0, 140), (80, 280), (0, 280)]
            self.alaoksa_v = [(0, 160), (100, 360), (0, 360)]
            # kuusi oikea
            self.ylaoksa_o = [(sx, 100), (sx-50, 200), (sx, 200)]
            self.keskioksa_o = [(sx, 140), (sx-80, 280), (sx, 280)]
            self.alaoksa_o = [(sx, 160), (sx-100, 360), (sx, 360)]
            # Vihreä väri RGB-arvoina
            self.vihrea = (70, 90, 65)
            naytto.fill(self.vihrea)
            naytto.fill((139, 178, 217))
            # Piirrä linna 
            naytto.blit(taustakuva, (sx / 2 - taustakuva.get_width() / 2, sy - taustakuva.get_height()))
            
            naytto.blit(puu, (0 - puu.get_width() / 2, sy - puu.get_height() - 10))
            naytto.blit(puu, (sx - puu.get_width() / 2 - 15, sy - puu.get_height() - 10))
            naytto.blit(lattia, (0, sy - lattia.get_height() + 18))




    def piirra_portti(self):
            naytto.blit(portti, (0, 480 - portti.get_height()))
            naytto.blit(portti, (sx - portti.get_width(), sy - portti.get_height()))


if __name__ == "__main__":
    Peli()