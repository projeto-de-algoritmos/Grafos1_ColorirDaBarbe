import sys 
sys.path.append("src/") 

from controller.graph import GraphController
import unittest
import numpy as np

class TestFloodBFS(unittest.TestCase):

    def test_blank_image(self):
        image = np.array([
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = GraphController(image)
        expected = np.array([
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],  
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],  
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]])
        graph.floodFill(0, 0, (1, 1, 1, 1))
        actual = graph.graph.image
        self.assertEqual(np.array_equal(actual, expected), True)

    def test_limited_pixel(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = GraphController(image)
        expected = np.array([
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph.floodFill(0, 0, (1, 1, 1, 1))
        actual = graph.graph.image
        self.assertEqual(np.array_equal(actual, expected), True)

    def test_limited_pixel_open_border(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = GraphController(image)
        expected = np.array([
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph.floodFill(0, 0, (1, 1, 1, 1))
        actual = graph.graph.image
        self.assertEqual(np.array_equal(actual, expected), True)

    def test_multiple_colors(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [2, 2, 2], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = GraphController(image)
        expected = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph.floodFill(1, 1, (1, 1, 1, 1))
        actual = graph.graph.image
        self.assertEqual(np.array_equal(actual, expected), True)

class TestFloodDFS(unittest.TestCase):
    def test_limited_pixel(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = GraphController(image, 'dfs')
        expected = np.array([
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph.floodFill(0, 0, (1, 1, 1, 1)) 
        actual = graph.graph.image
        self.assertEqual(np.array_equal(actual, expected), True)

    def test_limited_pixel_open_border(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = GraphController(image, 'dfs')
        expected = np.array([
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph.floodFill(0, 0, (1, 1, 1, 1))
        actual = graph.graph.image
        self.assertEqual(np.array_equal(actual, expected), True)

    def test_multiple_colors(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [2, 2, 2], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = GraphController(image, 'dfs')
        expected = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph.floodFill(1, 1, (1, 1, 1, 1))
        actual = graph.graph.image
        self.assertEqual(np.array_equal(actual, expected), True)

if __name__ == '__main__':
    unittest.main()
