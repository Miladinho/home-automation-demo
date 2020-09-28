from thermostat import Thermostat
from light import Light
import logging


class JSONFileNameError(Exception):
    def __init__(self, fileName):
        message = "File name \"{0}\" is not a JSON file".format(fileName)
        self.message = message
        super().__init__(message)

class BadHomeDataFileFormatError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
    
class InMemoryRepository:
    def __init__(self, fileService, fileName):
        if len(fileName) < 6 or fileName[-5:] != ".json":
            raise JSONFileNameError(fileName)
        self.data = {}
        self.dataFileName = fileName
        self.fileService = fileService
    
    def initFromDataFile(self):
        data = self.fileService.getComponents(self.dataFileName)
        if "components" not in data:
            raise BadHomeDataFileFormatError("Home data JSON file missing key \"{0}\"".format("components"))
        for comp in data["components"]:
            if comp["name"] in self.data:
                raise BadHomeDataFileFormatError("Duplicate component name \"{0}\" found in file".format(comp["name"]))
            if comp["type"] == "Thermostat":
                self.data[comp["name"]] = Thermostat(comp["name"], comp["temperature"])
            elif comp["type"] == "Light":
                self.data[comp["name"]] = Light(comp["name"], comp["status"])
            else:
                logging.warning("InMemoryRepository.initFromDataFile - Component with name \"{0}\" not recognized, will not be included in initial data".format(comp["name"]))
    
    def writeComponentsToFile(self):
        self.fileService.writeComponentsToFile(list(self.data.values()), self.dataFileName)

    def add(self, component):
        self.data[component.name] = component
        self.writeComponentsToFile()

    def remove(self, componentName):
        component = self.data.pop(componentName)
        self.writeComponentsToFile()
        return component

    def get(self, componentName):
        return self.data[componentName]

    def update(self, component):
        self.data[component.name] = component
        self.writeComponentsToFile()
        
    def isConnected(self, componentName):
        if componentName in self.data:
            return True
        return False

    def getLights(self):
        lights = []
        for component in self.data.values():
            if component.type == "Light":
                lights.append(component)
        return lights
