import unittest
from src.model.graph import Graph
class TestFloodFill(unittest.TestCase):

    def test_blank_image(self):
        image = [
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        graph = Graph(image)
        expected = [
            [1, 1, 1, 1], 
            [1, 1, 1, 1], 
            [1, 1, 1, 1], 
            [1, 1, 1, 1]]
        self.assertEqual(graph.floodFill(image, 0, 0, 1), expected)

    def test_limited_pixel(self):
        image = [
            [0, 1, 0, 0], 
            [1, 1, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        graph = Graph(image)
        expected = [
            [1, 1, 0, 0], 
            [1, 1, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        self.assertEqual(graph.floodFill(image, 0, 0, 1), expected)

    def test_limited_pixel_open_border(self):
        image = [
            [0, 1, 0, 0], 
            [1, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        graph = Graph(image)
        expected = [
            [1, 1, 0, 0], 
            [1, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        self.assertEqual(graph.floodFill(image, 0, 0, 1), expected)

    def test_multiple_colors(self):
        image = [
            [0, 1, 0, 0], 
            [1, 2, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        graph = Graph(image)
        expected = [
            [0, 1, 0, 0], 
            [1, 1, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        self.assertEqual(graph.floodFill(image, 1, 1, 1), expected)

if __name__ == '__main__':
    unittest.main()
