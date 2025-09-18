
import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1020, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # Janela redimensionável
pygame.display.set_caption("Mover Imagem com Setas")

BG_COLOR = (193, 0, 40)  # cor de fundo (um tom escuro)

image_file = "player.png"  # Coloque o nome correto da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()  # Carregar a imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Centraliza a imagem
else:
    print("Imagem do personagem não encontrada!")
    img = None
    img_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)  # Retângulo padrão para evitar erro

background_file = "background.png"  # Caminho para sua imagem de fundo
if os.path.exists(background_file):
    background_orig = pygame.image.load(background_file).convert()
    background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
else:
    background_orig = None
    background = None
    print("Imagem de fundo não encontrada!")

SPEED = 15  # pixels por movimento
JUMP_STRENGTH = 30  # Força do pulo (quanto maior, mais alto o pulo)
GRAVITY = 0.9  # Gravidade, fazendo o personagem cair
JUMPING = False  # Indica se o personagem está no ar
VELOCITY_Y = 0  # Velocidade no eixo Y (inicialmente sem velocidade de pulo)

def centralize_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)  # Centraliza a imagem no centro da tela

last_width, last_height = WIDTH, HEIGHT

def limit_movement():
    global img_rect, WIDTH, HEIGHT
    if img_rect.left < 0:
        img_rect.left = 0
    if img_rect.right > WIDTH:
        img_rect.right = WIDTH
    if img_rect.top < 0:
        img_rect.top = 0
    if img_rect.bottom > HEIGHT:
        img_rect.bottom = HEIGHT

def jump():
    global VELOCITY_Y, JUMPING
    if not JUMPING:
        VELOCITY_Y = -JUMP_STRENGTH  # Inicia o pulo para cima
        JUMPING = True

def update_jump():
    global VELOCITY_Y, JUMPING, img_rect
    if JUMPING:
        VELOCITY_Y += GRAVITY  # Simula a gravidade
        img_rect.y += VELOCITY_Y  # Atualiza a posição Y do personagem

        if img_rect.bottom >= HEIGHT:
            img_rect.bottom = HEIGHT  # Garante que o personagem não passe do chão
            JUMPING = False
            VELOCITY_Y = 0  # Reseta a velocidade no eixo Y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_width, current_height = screen.get_size()

    if current_width != last_width or current_height != last_height:
        WIDTH, HEIGHT = current_width, current_height
        centralize_image()  # Centraliza a imagem quando a janela mudar de tamanho
        if background_orig:
            background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))  # Redimensiona fundo a partir da original
        last_width, last_height = current_width, current_height

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        img_rect.x -= SPEED  # Move para a esquerda
    if keys[pygame.K_RIGHT]:
        img_rect.x += SPEED  # Move para a direita
    if keys[pygame.K_UP]:
        img_rect.y -= SPEED  # Move para cima
    if keys[pygame.K_DOWN]:
        img_rect.y += SPEED  # Move para baixo

    if keys[pygame.K_SPACE]:
        jump()  # Ativa o pulo

    limit_movement()

    update_jump()

    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(BG_COLOR)  # Caso não tenha fundo, mantém a cor de fundo

    if img:
        screen.blit(img, img_rect.topleft)

    pygame.display.flip()

pygame.quit()
