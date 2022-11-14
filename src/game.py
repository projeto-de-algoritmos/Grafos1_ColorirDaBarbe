from components.color_picker import ColorPicker
from components.draw import Draw

import pygame
import os
import random 

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption(("Colorir da Barbie"))

icon = pygame.image.load("public\\barbie-icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

cp = ColorPicker(50, 50, 400, 60)

path="assets"
files=os.listdir(path)
file=random.choice(files)

draw = Draw(100, 150, cp, image_path="assets\\" + file)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    cp.update()
    draw.update()

    screen.fill("white")
    cp.draw(screen)
    draw.draw(screen)

    pygame.display.flip()
     
    clock.tick(60)         

pygame.quit()
exit()
