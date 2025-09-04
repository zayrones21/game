import pygame

#inicializando o pygame
pygame.init()

#definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela Simples")

#Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    # Atualizar a tela
    pygame.display.flip()

    #Finalizar o pygame
    pygame.quit()