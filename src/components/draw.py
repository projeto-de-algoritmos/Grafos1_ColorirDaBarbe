from components.color_picker import ColorPicker
from model.draw_image import DrawImage
from model.graph import Graph
import numpy as np
import pygame

class Draw:
    def __init__(self, x: int, y: int, cp: ColorPicker, w: int = 300, h: int = 300, image_path: str = 'assets\\barbie.png') -> None:
        self.image = DrawImage(image_path)
        self.matriz = np.copy(self.image.getMatriz())
        self.graph = Graph(self.matriz)

        self.cp = cp

        self.rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.getSurface(), (0,0,0), self.rect)

    def getSurface(self) -> pygame.Surface:
        return pygame.surfarray.make_surface(self.matriz)
    
    def update(self) -> None:
        moude_buttons = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if moude_buttons[0] and self.rect.collidepoint((x, y)):
            self.matriz = self.graph.floodFill(self.matriz, x - 100, y - 150, self.cp.get_color())
    
    def draw(self, surf) -> None:
        surf.blit(self.getSurface(), self.rect)


