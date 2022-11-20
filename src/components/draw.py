from components.color_picker import ColorPicker
from controller.graph import GraphController
from model.draw_image import DrawImage
import numpy as np
import pygame
import threading

class Draw:
    def __init__(self, x: int, y: int, cp: ColorPicker, w: int = 300, h: int = 300, image_path: str = 'assets\\barbie.png') -> None:
        self.image = DrawImage(image_path)
        matriz = np.copy(self.image.getMatriz())
        self.graph = GraphController(matriz)

        self.cp = cp

        self.rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.getSurface(), (0,0,0), self.rect)

    def getSurface(self) -> pygame.Surface:
        return pygame.surfarray.make_surface(self.graph.graph.image)
    
    def update(self) -> None:
        moude_buttons = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if moude_buttons[0] and self.rect.collidepoint((x, y)):
            thread = threading.Thread(target= self.graph.floodFill, args=(x - 100, y - 150, self.cp.get_color()))
            thread.start()
           
    
    def draw(self, surf) -> None:
        surf.blit(self.getSurface(), self.rect)
