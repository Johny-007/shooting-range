import pygame
from pygame.locals import *
from pygame.surface import Surface, SurfaceType
from random import randint
from sys import exit
pygame.init()

# VARIAVEIS
tela_X = 640
tela_Y = 480

tela = pygame.display.set_mode((tela_X, tela_Y))
pygame.display.set_caption("Jogo do balão || Johny B. Santos")

clock = pygame.time.Clock()

tela_inicial0 = pygame.image.load("imagens/tela-inicial.png").convert()
tela_inicial = pygame.transform.scale(tela_inicial0, (tela_X, tela_Y))

mira01 = pygame.image.load("imagens/mira.png")
mira = pygame.transform.scale(mira01, (60, 60))

tela_fundo01 = pygame.image.load('imagens/tela-fundo.png').convert()
tela_fundo = pygame.transform.scale(tela_fundo01, (tela_X, tela_Y))

corBranco = (255,255,255)
corPreto = (0,0,0)
verdeCinza = (19, 43, 13)

pygame.mixer.music.set_volume(0.8)
trilha_sonora = pygame.mixer.music.load('sons/som-fundo.mp3')
pygame.mixer.music.play(-1)
atirou = pygame.mixer.Sound('sons/tiro.mp3')
clicou = pygame.mixer.Sound('sons/click.wav')
balao_estouro = pygame.mixer.Sound('sons/balao-estouro.mp3')

fonte01 = pygame.font.SysFont('arialblack', 25)
fonte02 = pygame.font.SysFont('arialblack', 13)
fonte03 = pygame.font.SysFont('bahnschrift', 27, True, True)

voltar = False

#BALAOOOO
balao1 = pygame.image.load("baloes/azul.png").convert_alpha()
balao1 = pygame.transform.scale(balao1, (138, 138))
rect_balon01 = balao1.get_rect()
mask1 = pygame.mask.from_surface(balao1)
balon_X = (tela_X / 2) - rect_balon01.center[0]
balon_Y = (tela_Y / 2) - rect_balon01.center[1]

mira_mask = pygame.mask.from_surface(mira)

# FUNÇÕES
def gerar_rect(cor, eixoX, eixoY, tamanoX, tamanhoY):
    pygame.draw.rect(tela, cor, (eixoX, eixoY, tamanoX, tamanhoY))


def gerar_texto(texto, fonte, corRGB, posicao_X, posicao_Y):
    texto_ = fonte.render(texto, True, corRGB)
    tela.blit(texto_, (posicao_X, posicao_Y))


def mouse_button(minimoX, maxX, miniY, maxY):  #verifica se o cursos está dentrodo parametros
    if minimoX <= mouse_cursor[0] <= maxX and miniY <= mouse_cursor[1] <= maxY:
        return True
    else:
        return False


while True:  #Loop Principal
    tela.fill((255,255,255))
    tela.blit(tela_inicial, (0, 0))
    mouse_cursor = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:

            if mouse_button(200, 445, 155, 195) == True:#CASO ABRA O BOTAO - JOGAR
                clicou.play()
                while True:
                    tela.fill(verdeCinza)
                    pygame.mouse.set_visible(False)
                    tela.blit(tela_fundo, (0, 0))
                    mouse_cursor = pygame.mouse.get_pos()

                    offset = mouse_cursor[0] - rect_balon01.x, mouse_cursor[1] - rect_balon01.y
                    #result = mask1.overlap_mask(mira_mask, offset)
                    touching = rect_balon01.collidepoint(*mouse_cursor) and mask1.get_at(offset)

                    if touching:
                        print("clicou, oh benção\n 1\n 55")


                    tela.blit(balao1, rect_balon01)
                    tela.blit(mira, (mouse_cursor[0] - 30, mouse_cursor[1] - 30))

                    if mouse_button(595, 630, 10, 25):
                        gerar_rect((10, 22, 6), 595, 10, 35, 15)
                        gerar_texto("...", fonte02, corBranco, 605, 4)
                    else:
                        gerar_rect((11, 11, 11), 595, 10, 35, 15)
                        gerar_texto("...", fonte02, corBranco, 605, 4)

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == MOUSEBUTTONDOWN:
                            tela.fill((255, 255, 0))
                            if mouse_button(595, 630, 10, 25):#CASO APERTE BOTAO VOLTAR
                                clicou.play()
                                voltar = True
                            else:# CASO ATIRE
                                atirou.play()


                    if voltar:
                        voltar = False
                        pygame.mouse.set_visible(True)
                        break

                    pygame.display.update()
                    clock.tick(30)

            if mouse_button(200, 445, 267, 307):#CASO ABRA OBOTAO - CRÉDITOS
                clicou.play()
                while True:
                    tela.fill(verdeCinza)
                    gerar_rect((10, 22, 6), 20, 20, 600, 440)

                    gerar_texto("Criador - Johny B. Santos", fonte03, corBranco, 30, 40)
                    gerar_texto("Data de Criação - 02/11/2022 ", fonte03, corBranco, 30, 80)
                    gerar_texto("GitHub - Johny-007", fonte03, corBranco, 30, 120)
                    gerar_texto("Linkdln - Johny Barbosa Santos", fonte03, corBranco, 30, 160)
                    gerar_texto("Versão - 0.1", fonte03, corBranco, 30, 200)
                    gerar_texto("Desing G. - Johny B. S. && Lavinya A. B.", fonte03, corBranco, 30, 240)

                    mouse_cursor = pygame.mouse.get_pos()
                    if mouse_button(200, 445, 400, 440) == True:
                        gerar_rect(verdeCinza, 200, 400, 245, 40)
                        gerar_texto("Voltar", fonte01, corBranco, 280, 400)
                    else:
                        gerar_rect(corPreto, 200, 400, 245, 40)
                        gerar_texto("Voltar", fonte01, corBranco, 280, 400)

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == MOUSEBUTTONDOWN:
                            if mouse_button(200, 445, 400, 440):#CASO APERTE BOTAO DE VOLTAR
                                clicou.play()
                                voltar = True
                    if voltar:
                        voltar = False
                        break
                    pygame.display.update()

    #BOTAO JOGAR
    if mouse_button(200, 445, 155, 195):
        gerar_rect((19,44,13), 200, 155, 245, 40)
        gerar_texto("JOGAR", fonte01, corBranco, 270, 156)
    else:
        gerar_rect(corPreto, 200, 155, 245, 40)
        gerar_texto("JOGAR", fonte01, corBranco, 270, 156)

    #BOTAO CRÉDITOS
    if mouse_button(200, 445, 267, 307):
        gerar_rect(verdeCinza, 200, 267, 245, 40)
        gerar_texto("CRÉDITOS", fonte01, corBranco, 257, 268)
    else:
        gerar_rect(corPreto, 200, 267, 245, 40)
        gerar_texto("CRÉDITOS", fonte01, corBranco, 257, 268)




    pygame.display.update()
    clock.tick(30)