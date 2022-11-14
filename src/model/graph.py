from collections import deque
from typing import List, Union
import numpy as np

RGBA = Union[int, int, int, int]

class Graph:

    def __init__(self, image: List[List[List[int]]]) -> None:
        self.image = image

    def floodFill(self, image: List[List[List[int]]], sr: int, sc: int, newColor: RGBA) -> List[List[List[int]]]:
        """
        A queue implementing the Breadth First Search algorithm to flood fill the image.
        image is the graph
        (sr, sc) is the position of pixel
        newColor is the new color
        """
        R, C, RGB = image.shape
        color = np.copy(image[sr][sc]) 

        r, g, b, a = newColor
        newColor = [r, g, b]
          
        Q = deque([(sr, sc)])
        seen = set()
        while Q:
            r, c = Q.popleft()
            image[r][c] = newColor
            if (r, c) in seen:
                continue
            seen.add((r, c))
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and image[nr][nc].all() == color.all():
                    Q.append((nr, nc))
        return image
