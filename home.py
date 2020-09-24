class Home:
    def __init__(self):
        self.data = {}
    
    def add(self, component):
        if not self.isConnected(component.name):
            self.data[component.name] = component
        else:
            raise Exception("Component Already Connected")

    def remove(self, componentName):
        return self.data.pop(componentName)
        
    def isConnected(self, componentName) -> bool:
        if componentName in self.data:
            return True
        return False
