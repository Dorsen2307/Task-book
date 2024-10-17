class CurrentError(Exception):
    pass

class InputValueError(CurrentError):
    def __init__(self, message = 'The value was not found.'):
        self.message = message
        super().__init__(self.message)

class DBNotFoundError(CurrentError):
    def __init__(self, message = 'File not found.'):
        self.message = message
        super().__init__(self.message)