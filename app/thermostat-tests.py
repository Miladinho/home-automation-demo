import unittest
from unittest.mock import Mock, MagicMock
from home import Home
from thermostat import Thermostat

class ThermostatTests(unittest.TestCase):
    def setUp(self):
        self.home = Home(Mock())
    
    def test_read_temperature(self):
        # Here a quick stub to replace a query method is more convenient
        self.home.repository.get = MagicMock(return_value=Thermostat("Thermostat",temp=68))
        self.assertEqual(self.home.getTemperature(), 68)
    
    def test_set_temperature(self):
        class RepositorySetTempMock():
            def update(self, component):
                self.temp = component.temperature
        self.home = Home(RepositorySetTempMock())
        self.home.setTemperature(75)
        self.assertEqual(self.home.repository.temp, 75)

    def test_get_thermostat(self):
        thermo = Thermostat("Thermostat",temp=68)
        self.home.repository.get = MagicMock(return_value=thermo)
        self.assertEqual(self.home.getThermostat(), thermo)
if __name__ == '__main__':
    unittest.main()
