from collections import deque
from typing import List, Union

from model.graph import Graph

RGBA = Union[int, int, int, int]

class GraphController:

    def __init__(self, image: List[List[List[int]]], algorithm: str= 'bfs') -> None:
        self.graph = Graph(image)
        self.algorithm = algorithm

    def setAlgorithm(self) -> None:
        if self.algorithm == 'bfs':
            self.algorithm = 'dfs'
        elif self.algorithm == 'dfs':
            self.algorithm = 'bfs'
        self.graph.duration = 0

    def getAlgorithm(self) -> str:
        return self.algorithm
    
    def floodFill(self, sr: int, sc: int, newColor: RGBA) -> None:
        """
        image is the graph
        (sr, sc) is the position of pixel
        newColor is the new color
        """
        if self.algorithm == 'bfs':
            self.graph.bfs(sr, sc, newColor)
        elif self.algorithm == 'dfs':
            self.graph.dfs(sr, sc, newColor)

        return
