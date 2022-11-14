from src.model.graph import Graph

import unittest
import numpy as np

class TestFloodFill(unittest.TestCase):

    def test_blank_image(self):
        image = np.array([
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = Graph(image)
        expected = np.array([
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],  
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],  
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]])
        actual = graph.floodFill(image, 0, 0, (1, 1, 1, 1))
        self.assertEqual(actual.all(), expected.all())

    def test_limited_pixel(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = Graph(image)
        expected = np.array([
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        actual = graph.floodFill(image, 0, 0, (1, 1, 1, 1))    
        self.assertEqual(actual.all(), expected.all())

    def test_limited_pixel_open_border(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = Graph(image)
        expected = np.array([
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        actual = graph.floodFill(image, 0, 0, (1, 1, 1, 1))
        self.assertEqual(actual.all(), expected.all())

    def test_multiple_colors(self):
        image = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [2, 2, 2], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        graph = Graph(image)
        expected = np.array([
            [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        actual = graph.floodFill(image, 1, 1, (1, 1, 1, 1))
        self.assertEqual(actual.all(), expected.all())

if __name__ == '__main__':
    unittest.main()
