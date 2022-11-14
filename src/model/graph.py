from collections import deque

from timeit import default_timer as timer
from typing import List, Union
import numpy as np

RGBA = Union[int, int, int, int]

class Graph:

    def __init__(self, image: List[List[List[int]]]) -> None:
        self.image = image
        self.duration = 0

    def bfs(self, image: List[List[List[int]]], sr: int, sc: int, newColor: RGBA) -> List[List[List[int]]]:
        """
        A queue implementing the Breadth First Search algorithm to flood fill the image.
        """
        start = timer()
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
                if 0 <= nr < R and 0 <= nc < C and np.array_equal(image[nr][nc], color):
                    Q.append((nr, nc))
        end = timer()
        self.duration = end - start
        return image

    def dfs(self, image: List[List[List[int]]], sr: int, sc: int, newColor: RGBA) -> List[List[List[int]]]:
        """
        A stack implementing the Depth First Search Algorithm to flood fill the image.
        """
        start = timer()
        R, C, RGB = image.shape
        color = np.copy(image[sr][sc])

        r, g, b, a = newColor
        newColor = [r, g, b]
          
        st = [(sr, sc)]
        seen = set()
        while st:
            r, c = st.pop(0)
            image[r][c] = newColor
            if (r, c) in seen:
                continue
            seen.add((r, c))
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and np.array_equal(image[nr][nc], color):
                    st.append((nr, nc))
        end = timer()
        self.duration = end - start
        return image
