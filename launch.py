import pygame
import main
import math
pygame.init()

window = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
player = main.Player((150,150))
game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.events(event)
    window.fill((0,0,0))
    window.blit(player.image, player.rect)

    clock.tick(30)
    pygame.display.update()