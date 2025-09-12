import pygame
pygame.init() # Inicializa o pygame
largura = 800 # Define a largura
altura = 600 # Define a altura da tela
tela = pygame.display.set_mode((largura, altura)) # Cria a tela com as dimensões especificadas
pygame.display.set_caption("Exemplo de Jogo") # Define o título da janela
rodando = True # Variável para controlar o loop principal
while rodando: # Loop principal do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((64,224,208)) # Preenche a tela com preto
    pygame.display.update() # Atualiza a tela

pygame.quit() # Encerra a tela