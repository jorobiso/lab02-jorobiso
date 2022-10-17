import unittest
import vehicle
class VehicleTests(unittest.TestCase):
   def test_vehicle(self):

      result = vehicle.Vehicle(4, 14.8, 4, True)
      self.assertEqual(result.wheels, 4)
      self.assertEqual(result.fuel, 14.8)
      self.assertEqual(result.doors, 4)
      self.assertEqual(result.roof, True)


        # 1) Create a Vehicle with values of your choice.
        # 2) Use assertEqual or assertAlmostEqual on each field in
        #    the new Vehicle to verify that it holds the expected value.


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

