from controller.graph import GraphController
import pygame

class Label:
    def __init__(self, x: int, y: int, graph: GraphController, font: int = 14) -> None:
        self.graph = graph
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("Arial", font)

    def draw(self, surf) -> None:
        self.label = self.font.render(f" O algoritmo {self.graph.getAlgorithm()} teve a duração de {self.graph.graph.duration}", 1, pygame.Color("black"))
        surf.blit(self.label, (self.x,self.y))
