class CurrentError(Exception):
    pass

class InvalidInputError(Exception):
    def __init__(self, message = 'The value was not found.'):
        self.message = message
        super().__init__(self.message)

class DBNotFoundError(Exception):
    def __init__(self, message = 'File not found.'):
        self.message = message
        super().__init__(self.message)