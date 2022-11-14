from components.color_picker import ColorPicker
from components.draw import Draw

import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption(("Colorir da Barbie"))

clock = pygame.time.Clock()

cp = ColorPicker(50, 50, 400, 60)

draw = Draw(120, 50, cp)

surf = draw.getSurface()
screen.blit(surf, (120, 50))

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
