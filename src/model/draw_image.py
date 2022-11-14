from typing import List

import pygame

class DrawImage:
    def __init__(self, image_path: str) -> None:
        self.image_path = image_path

    def getMatriz(self) -> List[List[str]]: 
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.matriz = pygame.surfarray.pixels3d(self.image)

        return self.matriz
