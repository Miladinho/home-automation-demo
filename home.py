class Home:
    def __init__(self):
        self.data = {}
    
    def add(self, component):
        if not self.isConnected(component):
            self.data[component.name] = component
        else:
            raise Exception("Component Already Connected")

    def isConnected(self, component) -> bool:
        if component.name in self.data:
            return True
        return False
