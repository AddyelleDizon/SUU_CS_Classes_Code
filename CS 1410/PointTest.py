import unittest
from Point import Point

class TestPoint(unittest.TestCase):
    
    # Tests the constructor: default values
    def test_default_constructor(self):
        point = Point()
        self.assertEqual(point.get_x(), 0)
        self.assertEqual(point.get_y(), 0)
    
    # Tests the constructor: with differing values
    def test_parameterized_constructor(self):
        point = Point(1, 2)
        self.assertEqual(point.get_x(), 1)
        self.assertEqual(point.get_y(), 2)
    
    # Tests the numeric value for the x-value
    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Point("x", 2)
    
    # Tests the numeric value for the y-value
    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Point(1, "y")
    
    # Tests the TypeError for the x-value
    def test_set_x_invalid(self):
        point = Point()
        with self.assertRaises(TypeError):
            point.set_x("x")
    
    # Tests the TypeError for the y-value
    def test_set_y_invalid(self):
        point = Point()
        with self.assertRaises(TypeError):
            point.set_y("y")
    
    # Tests the clone method
    def test_clone(self):
        point_1 = Point(10, 10)
        point_2 = point_1.clone()
        self.assertEqual(point_1.get_x(), point_2.get_x())
        self.assertEqual(point_1.get_y(), point_2.get_y())
        self.assertIsNot(point_1, point_2)

    # Tests the distance method
    def test_distance(self):
        point_1 = Point(0, 0)
        point_2 = Point(3, 4)
        self.assertEqual(point_1.distance(point_2), 5.0)
        
    # Tests the TypeError for the distance    
    def test_distance_invalid_type(self):
        point = Point(0, 0)
        with self.assertRaises(TypeError):
            point.distance((3, 4))
    
    # Tests the string method
    def test_str_method(self):
        point = Point(1, 2)
        self.assertEqual(str(point), "X: 1, Y: 2")

def main():
    unittest.main()

if __name__ == "__main__":
    main()