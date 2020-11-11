import pygame
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit

pygame.init()

#setamos o tamanho da tela
tela  = pygame.display.set_mode((600, 600), 0, 32)
#Título da janela do jogo
pygame.display.set_caption('Jogo da velha')

ESTADO = 'JOGANDO'
VEZ = 'JOGADOR1'
ESCOLHA = 'X'
imagemFundo = pygame.image.load('imagens/fundo.jpg')

WHITE = (255, 255, 255)

marca_tabu = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]
#definimos retângulos dentro do espaço de cada casa do tabuleiro
rect1 = Rect((10,200), (204, 330))
rect2 = Rect((204,200), (397, 330))
rect3 = Rect((397,200), (590, 330))
rect4 = Rect((10,330), (204, 470))
rect5 = Rect((204,330), (397, 470))
rect6 = Rect((397,330), (590, 470))
rect7 = Rect((10,470), (204, 600))
rect8 = Rect((204,470), (397, 600))
rect9 = Rect((397,470), (590, 600))

#lista com os retângulos das casas dos tabuleiros
rec = [
    rect1, rect2, rect3, rect4,
    rect5, rect6, rect7, rect8, rect9,
]
#função responsável por desenhar as linhas do tabuleiro
def desenhar_tabu():
    pygame.draw.line(tela, WHITE, (204, 200), (204, 600), 10)
    pygame.draw.line(tela, WHITE, (397, 200), (397, 600), 10)
    pygame.draw.line(tela, WHITE, (10, 330), (590, 330), 10)
    pygame.draw.line(tela, WHITE, (10, 470), (590, 470), 10)

def menu():
    #Definem-se os estilos e tamanhos das fontes usados no menu
    fonte = pygame.font.SysFont('goudy stout', 40)
    fonte2 = pygame.font.SysFont('goudy stout', 25)
    fonte3 = pygame.font.SysFont('forte', 18)
    #Definem-se os textos, cores e atribuímos à variáveis
    titulo1 = fonte.render('Jogo', True, WHITE, 0)
    titulo2 = fonte.render('da', True, WHITE, 0)
    titulo3 = fonte.render('Velha', True, WHITE, 0)
    opcaoJogar = fonte2.render('Jogar', True, WHITE, 0)
    opcaoRanking = fonte2.render('Ranking', True, WHITE, 0)
    credito = fonte3.render('By: Gabriel Batista / Julia Carvalho / Fabio Silveira', True, (255, 255, 255), 0)
    
    #Comandos para posicionar os textos na tela
    tela.blit(titulo1, (200, 40))
    tela.blit(titulo2, (250, 90))
    tela.blit(titulo3, (170, 140))
    tela.blit(opcaoJogar, (220, 350))
    tela.blit(opcaoRanking, (190, 410))
    tela.blit(credito, (97, 570))




while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()
    tela.blit(imagemFundo, (0,0))
    menu()
    #desenhar_tabu()
    pygame.display.flip()

