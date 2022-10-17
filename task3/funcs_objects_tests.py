import unittest
import objects
import funcs_objects
import math


class TestCases(unittest.TestCase):
   def test_point(self):
      test_point = objects.Point(4.0,5.0)
      # Add code here to verify that a point is initialized correctly.
      self.assertEqual(test_point.x, 4.0)
      self.assertEqual(test_point.y, 5.0)


   def test_circle(self):
      test_circle = objects.Circle(objects.Point(4.5, 5.6), 4.0)
      self.assertEqual(test_circle.center.x, 4.5)
      self.assertEqual(test_circle.center.y, 5.6)
      self.assertEqual(test_circle.r, 4.0)
      # Add code here to verify that a circle is initialized correctly.


   # Add other testing functions for distance and circles_overlap.
   def test_distance(self):
      c_one = objects.Circle(objects.Point(4.0,0.0), 4.0)
      c_two = objects.Circle(objects.Point(6.0, 0.0), 9.0)

      self.assertEqual(c_one.center.x, 4.0)
      self.assertEqual(c_one.center.y, 0.0)
      self.assertEqual(c_two.center.x, 6.0)
      self.assertEqual(c_two.center.y, 0.0)

      self.assertEqual(math.sqrt((c_two.center.x - c_one.center.x)**2 + (c_two.center.y - c_one.center.y)**2), 2.0)

   def test_circles_overlap(self):
      c_one = objects.Circle(objects.Point(4.0, 0.0), 4.0)
      c_two = objects.Circle(objects.Point(6.0, 0.0), 9.0)
      self.assertEqual(math.sqrt((c_two.center.x - c_one.center.x)**2 + (c_two.center.y - c_one.center.y)**2) < (c_one.r + c_two.r), True)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

