from controller.graph import GraphController
import pygame

class Button:
    def __init__(self, x: int, y: int, graph: GraphController, font: int = 45, w: int = 30, h: int = 30) -> None:
        self.graph = graph
        self.font = pygame.font.SysFont("Arial", font)
        self.surface = pygame.Surface((x, y))
        self.rect = pygame.Rect(x, y, w, h)
        self.changeText()

    def changeText(self) -> None:
        self.text = self.font.render(self.graph.getAlgorithm(), 1, pygame.Color("White"))
        self.surface.fill((170,170,170))
        self.surface.blit(self.text, (0, 1))
    
    def update(self) -> None:
        moude_buttons = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if moude_buttons[0] and self.rect.collidepoint((x, y)):
            self.graph.setAlgorithm()
            self.changeText()
    
    def draw(self, surf) -> None:
        surf.blit(self.surface, self.rect)
