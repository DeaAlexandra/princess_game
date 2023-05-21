import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))
taustakuva = pygame.image.load("castle_background.png")
puu = pygame.image.load("tree.png")
lattia = pygame.image.load("stone_floor_wide.png")
princess = pygame.image.load("princess_1.png")
ovi = pygame.image.load("gate.png")
hirvio = pygame.image.load("dragon.png")
sx, sy = naytto.get_size()

y = sy - princess.get_height()
nopeus = 5
naytto.fill((139, 178, 217))


class Hirvio:
    osui = False
    vaistetyt = 0
    def __init__(self):
        self.hirvio = hirvio
        self.x = random.randrange(ovi.get_width(), sx - ovi.get_width() - hirvio.get_width())
        self.y = -(random.randrange(20, sy - hirvio.get_height()))
        self.v = random.randrange(1, nopeus)
    def game_over(self):
        if Hirvio.osui != True:
            self.y += self.v
    def osuma(self,princess_x,princess_y):
        if self.y > sy - princess.get_height() - hirvio.get_height():
            if princess_x + princess.get_width() < self.x or princess_x  > self.x + 40:
                pass
            else:
                Hirvio.osui = True
    def nollaa(self):
        self.x = random.randrange(ovi.get_width(), sx - ovi.get_width())
        self.y = -(random.randrange(20, 480 - hirvio.get_height()))
        self.v = random.randrange(1, 5)


class Peli:
    def __init__(self):
        pygame.init()
        #värit
        self.white = (255, 255, 255)
        self.green = (70, 90, 65)
        self.blue = (0, 0, 128)
        self.yellow = (175, 155, 125)
        self.dark_grey = (59, 56, 56)
        self.black = (0, 0, 0)

        pygame.display.set_caption('Väistä hirviötä')
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.font_a = pygame.font.Font('freesansbold.ttf', 18)
        self.font_b = pygame.font.Font('freesansbold.ttf', 14)
        self.help = False
        self.suunta = 0
        self.princess_x = 100
        self.princess_y = 480 - princess.get_height()
        self.game_over = False
        self.help = False

        self.kello = pygame.time.Clock()
        naytto.fill((139, 178, 217))
        self.piirra_tausta()
        self.piirra_ovet()
        self.aloitusikkuna()
        txtsurf_a = self.font.render("Aloita peli = välilyönti", True, self.dark_grey)
        naytto.blit(txtsurf_a,(160,140))
        pygame.display.flip()


        self.hirviolista = []
        for i in range(1,random.randrange(5,10)):
            self.hirviolista.append(Hirvio())

        self.silmukka()

    def silmukka(self):
        game_running = True

        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Aloita peli
     
                        self.tutki_tapahtumat()

    def aloitusikkuna(self):
        txtsurf_b = self.font_a.render("Pelin tarkoituksena on väistellä lohikäärmeitä joita laskeutuu taivaalta.", True, self.dark_grey)
        naytto.blit(txtsurf_b,(30,20))
        txtsurf_b = self.font_a.render("prinsessaa ohjataan oikealle ja vasemmalle nuolinäppäimillä.", True, self.dark_grey)
        naytto.blit(txtsurf_b,(60,60))
        txtsurf_b = self.font_a.render("Voit siirtyä reunasta toiseen myös porttien kautta, mutta varo lohikäärmeitä.", True, self.dark_grey)
        naytto.blit(txtsurf_b,(20,100))

        self.princess = princess
        xa = self.princess_x = sx // 2 - princess.get_width()
        ya = self.princess_y = sy - princess.get_height()
        naytto.blit(self.princess, (xa, ya))


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
                        for k in self.hirviolista:
                            self.hirviolista = []
                            for i in range(1,random.randrange(5,10)):
                                self.hirviolista.append(Hirvio())
                        Hirvio.osui = False
                        Hirvio.vaistetyt = 0
                    if tapahtuma.key == pygame.K_F1:
                        self.help = True
                    if tapahtuma.key == pygame.K_ESCAPE:
                       self.help = False
                if tapahtuma.type == pygame.QUIT:
                    exit()
            naytto.fill((139, 178, 217))
            self.piirra_tausta()
            self.piirra_ovet()
            self.hirvion_kasittely()


    def hirvion_kasittely(self):
        #hirvion kasittely
        if self.help == False:
            for k in self.hirviolista:
                k.game_over()
                k.osuma(self.princess_x,self.princess_y)
                if k.y < 400:
                    naytto.blit(k.hirvio, (k.x, k.y))
                else:
                    Hirvio.vaistetyt += 1
                    print(Hirvio.vaistetyt)
                    k.nollaa()
            if Hirvio.osui == True:
                self.suunta = 0
            else:
                if self.suunta == 1:
                    self.princess_x += nopeus
                    if self.princess_x >= sx - princess.get_width() - ovi.get_width() // 2:
                        self.princess_x = 0 + ovi.get_width() // 2

                if self.suunta == 2 and self.princess_x >= 0 + ovi.get_width() // 2:
                    self.princess_x -= nopeus
                    if self.princess_x <= 0 + ovi.get_width() // 2:
                        self.princess_x = sx - princess.get_width() - ovi.get_width() // 2

        naytto.blit(self.princess, (self.princess_x, self.princess_y))
        # pisteet näytölle
        if Hirvio.vaistetyt < 10:
            txtsurf = self.font.render(f"{Hirvio.vaistetyt}", True, self.white)
            naytto.blit(txtsurf,(sx // 2 - 10, 210))

        else:
            txtsurf = self.font.render(f"{Hirvio.vaistetyt}", True, self.white)
            naytto.blit(txtsurf,(sx // 2 - 15, 210))
        # pisteiden selite näytölle
        txtsurf = self.font_b.render(f"pisteet", True, self.white)
        naytto.blit(txtsurf,(sx // 2 - 25, 235))
        if Hirvio.osui == True:
            txtsurf = self.font.render(f" Hävisit. Onnistuit väistämään {Hirvio.vaistetyt} hirviötä", True, self.yellow, self.dark_grey)
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




    def piirra_ovet(self):
            naytto.blit(ovi, (0, 480 - ovi.get_height()))
            naytto.blit(ovi, (sx - ovi.get_width(), sy - ovi.get_height()))


if __name__ == "__main__":
    Peli()


