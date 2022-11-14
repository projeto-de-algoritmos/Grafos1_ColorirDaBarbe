import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("white")

    pygame.display.flip()
     
    clock.tick(60)         

pygame.quit()
exit()
