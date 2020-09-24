import unittest
from light import Light
from home import Home

class LightTests(unittest.TestCase):
    def test_add_new_light(self):
        newLight = Light("test")
        home = Home()
        home.add(newLight)
        self.assertTrue(home.isConnected(newLight))

    def test_add_existing_light_throws(self):
        light = Light("test")
        home = Home()
        home.add(light)
        self.assertRaises(Exception, home.add, **{"component": light})
    

        
if __name__ == '__main__':
    unittest.main()
