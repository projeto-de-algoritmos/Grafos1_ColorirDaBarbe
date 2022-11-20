from collections import deque

from timeit import default_timer as timer
from typing import List, Union
import numpy as np
import time
import sys

RGBA = Union[int, int, int, int]

class Graph:

    def __init__(self, image: List[List[List[int]]], running: bool= True) -> None:
        self.image = image
        self.duration = 0
        self.running = running

    def bfs(self, sr: int, sc: int, newColor: RGBA) -> None:
        """
        A queue implementing the Breadth First Search algorithm to flood fill the image.
        """
        start = timer()
        R, C, RGB = self.image.shape
        color = np.copy(self.image[sr][sc])

        r, g, b, a = newColor
        newColor = [r, g, b]
          
        Q = deque([(sr, sc)])
        seen = set()
        while Q:
            if not self.running:
                sys.exit(0)
            r, c = Q.popleft()
            self.image[r][c] = newColor
            time.sleep(0.0000000001)
            if (r, c) in seen:
                continue
            seen.add((r, c))
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and np.array_equal(self.image[nr][nc], color):
                    Q.append((nr, nc))
        end = timer()
        self.duration = end - start

    def dfs(self, sr: int, sc: int, newColor: RGBA) -> None:
        """
        A stack implementing the Depth First Search Algorithm to flood fill the image.
        """
        start = timer()
        R, C, RGB = self.image.shape
        color = np.copy(self.image[sr][sc])

        r, g, b, a = newColor
        newColor = [r, g, b]
          
        st = [(sr, sc)]
        seen = set()
        while st:
            if not self.running:
                sys.exit(0)
            r, c = st.pop()
            self.image[r][c] = newColor
            time.sleep(0.0000000001)
            if (r, c) in seen:
                continue
            seen.add((r, c))
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and np.array_equal(self.image[nr][nc], color):
                    st.append((nr, nc))
        end = timer()
        self.duration = end - start
