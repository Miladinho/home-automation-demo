class ComponentNotConnectedError(Exception):
    def __init__(self, componentName):
        message = "Component with name "+"\""+componentName+"\""+" is not connected."
        self.message = message
        super().__init__(message)
    def __str__(self):
        return "ComponentNotConnectedError: {0}".format(self.message)

class ComponentAlreadyConnectedError(Exception):
    def __init__(self, componentName):
        message = "Component with name "+"\""+componentName+"\""+" is already connected."
        self.message = message
        super().__init__(message)
    def __str__(self):
        return "ComponentAlreadyConnectedError: {0}".format(self.message)
