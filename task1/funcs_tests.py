import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      result = funcs.f(1)
      self.assertEqual(result, 9)

   def test_f_2(self):
      result = funcs.g(1,2)
      self.assertEqual(result, 5)

   def test_f_3(self):
      result = funcs.hypotenuse(3,4)
      self.assertEqual(result, 5)

   def test_f_4(self):
      result = funcs.is_positive(5)
      self.assertEqual(result, True)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
