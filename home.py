from errors import *

class Home:
    def __init__(self):
        self.data = {}
    
    def add(self, component):
        if not self.isConnected(component.name):
            self.data[component.name] = component
        else:
            raise Exception("Component Already Connected")

    def remove(self, componentName):
        if self.isConnected(componentName):
            return self.data.pop(componentName)
        raise ComponentDoesNotExistError(componentName)
        
    def isConnected(self, componentName) -> bool:
        if componentName in self.data:
            return True
        return False
