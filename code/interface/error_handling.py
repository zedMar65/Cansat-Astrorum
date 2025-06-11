class ErrorHandler(ABC):
    @classmethod
    def async_error(cls, e: Exception):
        pass

# Custom Error classes
class InnerError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = "Inner Failure: " + message

class LogError(InnerError):
    def __init__(self, message):
        self.message = f"Error while logging: \n{message}"
        super().__init__(self.message)
