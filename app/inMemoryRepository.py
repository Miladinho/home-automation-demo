class InMemoryRepository():
    def __init__(self):
        self.data = {}
    
    def add(self, component):
        self.data[component.name] = component

    def remove(self, componentName):
        return self.data.pop(componentName)

    def get(self, componentName):
        return self.data[componentName]

    def update(self, component):
        self.data[component.name] = component
        
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
