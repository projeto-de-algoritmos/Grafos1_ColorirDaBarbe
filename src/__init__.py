from components.color_picker import ColorPicker

import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

cp = ColorPicker(50, 50, 400, 60)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    cp.update()

    screen.fill("white")
    cp.draw(screen)

    pygame.display.flip()
     
    clock.tick(60)         

pygame.quit()
exit()
