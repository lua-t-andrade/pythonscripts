import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("THIS IS A TEST")

rect_1 = pygame.Rect(0, 0, 25, 25)
rect_2 = pygame.Rect(random.randint(0, 600), random.randint(0, 600), 25, 25)
border_1 = pygame.Rect(0, 0, 10, 600)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    if rect_1.colliderect(rect_2): 
        rect_2 = pygame.Rect(random.randint(0, 600), random.randint(0, 600), 25, 25)
        pygame.draw.rect(screen, "red", rect_2)

    pos = pygame.mouse.get_pos()
    rect_1.center = pos
    
    pygame.draw.rect(screen, "black", rect_1)
    pygame.draw.rect(screen, "red", rect_2)
    pygame.draw.rect(screen, "black", border_1)

    pygame.display.flip()

pygame.quit()