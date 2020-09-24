class ComponentDoesNotExistError(Exception):
    def __init__(self, componentName):
        super().__init__(f"Component with name \"{componentName}\" does not exist.")
