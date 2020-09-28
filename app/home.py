from errors import *
from thermostat import Thermostat
from light import Light

import logging
logging.basicConfig(filename='home.log',level=logging.DEBUG)

class Home:
    def __init__(self, repository):
        self.repository = repository

    def initBaseComponents(self):
        self.repository.add(Thermostat("Thermostat",temp=68))
        self.repository.add(Light("Living Room Light"))
        logging.info("Initialized 1 thermostat and 1 light in memory")

    def isConnected(self, componentName):
        return self.repository.isConnected(componentName)

    def getTemperature(self):
        return self.repository.get("Thermostat").temperature

    def setTemperature(self, newValue):
        self.repository.update(Thermostat("Thermostat",temp=newValue))
        logging.info("Set temperature to \"{0}\"".format(newValue))

    def addLight(self, name, status=0):
        if not self.repository.isConnected(name):
            self.repository.add(Light(name,status))
            logging.info("Added new light \"{0}\"".format(name))
        else:
            e = ComponentAlreadyConnectedError(name)
            logging.exception("addLight -" + e.__str__())
            raise e
    
    def removeLight(self, name):
        if self.repository.isConnected(name):
            logging.info("Removed light \"{0}\"".format(name))
            return self.repository.remove(name).name
        e = ComponentNotConnectedError(name)
        logging.exception("removeLight - " + e.__str__())
        raise e

    def getLightStatus(self, name):
        if self.repository.isConnected(name):
            return self.repository.get(name).status
        e = ComponentNotConnectedError(name)
        logging.exception("getLightStatus - " + e.__str__())
        raise e

    def setLightStatus(self, name, value):
        if self.repository.isConnected(name):
            self.repository.update(Light(name,value))
            logging.info("Set light \"{0}\" to {1}".format(name, value))
        else:
            e = ComponentNotConnectedError(name)
            logging.exception("setLightStatus - " + e.__str__())
            raise e
    
    def getLights(self):
        return self.repository.getLights()

    def getThermostat(self):
        return self.repository.get("Thermostat")
