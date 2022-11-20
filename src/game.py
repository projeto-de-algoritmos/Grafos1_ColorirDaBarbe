from components.button import Button
from components.color_picker import ColorPicker
from components.draw import Draw
from components.label import Label

import pygame
import os
import random 

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption(("Colorir da Barbe"))

clock = pygame.time.Clock()

cp = ColorPicker(50, 50, 400, 60)

path="assets"
files=os.listdir(path)
file=random.choice(files)

draw = Draw(100, 150, cp, image_path="assets\\" + file)
button = Button(450, 450, draw.graph)
label = Label(80,450, draw.graph)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draw.graph.graph.running = False
            pygame.quit()
            raise SystemExit

    cp.update()
    draw.update()
    button.update()

    screen.fill("white")
    cp.draw(screen)
    draw.draw(screen)
    button.draw(screen)
    label.draw(screen)

    pygame.display.flip()
     
    clock.tick(60)         

pygame.quit()
exit()
