from errors import *
from thermostat import Thermostat
from light import Light

class Home:
    def __init__(self, repository):
        self.repository = repository

    def isConnected(self, componentName):
        return self.repository.isConnected(componentName)

    def getTemperature(self):
        return self.repository.get("Thermostat").temperature

    def setTemperature(self, newValue):
        self.repository.update(Thermostat("Thermostat",temp=newValue))

    def addLight(self, name, status=0):
        if not self.repository.isConnected(name):
            self.repository.add(Light(name,status))
        else:
            raise ComponentAlreadyConnectedError(name)
    
    def removeLight(self, name):
        if self.repository.isConnected(name):
            return self.repository.remove(name).name
        raise ComponentNotConnectedError(name)

    def getLightStatus(self, name):
        if self.repository.isConnected(name):
            return self.repository.get(name).status
        raise ComponentNotConnectedError(name)

    def setLightStatus(self, name, value):
        if self.repository.isConnected(name):
            self.repository.update(Light(name,value))
        else:
            raise ComponentNotConnectedError(name)
    
    def getLights(self):
        return self.repository.getLights()

    def getThermostat(self):
        return self.repository.get("Thermostat")
