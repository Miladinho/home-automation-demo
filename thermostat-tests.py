import unittest
from home import Home
from thermostat import Thermostat

class ThermostatTests(unittest.TestCase):
    def setUp(self):
        self.home = Home()
        self.home.add(Thermostat("thermostat", temp=68))
    
    def test_read_temperature(self):
        self.assertEqual(self.home.get("thermostat").temperature, 68)
    
    def test_set_temperature(self):
        thermostat = self.home.get("thermostat")
        thermostat.temperature = 75
        self.home.update(thermostat)
        self.assertEqual(self.home.get("thermostat").temperature, 75)

if __name__ == '__main__':
    unittest.main()
