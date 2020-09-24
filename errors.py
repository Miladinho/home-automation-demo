class ComponentNotConnectedError(Exception):
    def __init__(self, componentName):
        super().__init__(f"Component with name \"{componentName}\" is not connected.")

class ComponentAlreadyConnectedError(Exception):
    def __init__(self, componentName):
        super().__init__(f"Component with name \"{componentName}\" is already connected.")
