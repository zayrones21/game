import pygame
import os

#inicializando o pygame
pygame.init()

#definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela com Imagem")

#Definindo  a cor de fundo
BG_COLOR = (30, 30, 40) # cor de fundo (um tom escuro)

#Carregar imagem
image_file = "player.png"
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
else:
    print("Imagem não encontrada!")

#Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    #preencher o fundo
    screen.fill(BG_COLOR)

    #desenhar a imagem na tela
    screen.blit(img, img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

    #Finalizar o pygame
    pygame.quit()