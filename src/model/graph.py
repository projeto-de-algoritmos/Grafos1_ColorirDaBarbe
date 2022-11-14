from collections import deque
from typing import List

class Graph:

    def __init__(self, image:  List[List[int]]) -> None:
        self.image = image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        A queue implementing the Breadth First Search algorithm to flood fill the image.
        image is the graph
        (sr, sc) is the position of pixel
        newColor is the new color
        """
        R, C = len(image), len(image[0])
        color = image[sr][sc]
          
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
                if 0 <= nr < R and 0 <= nc < C and image[nr][nc] == color:
                    Q.append((nr, nc))
        return image