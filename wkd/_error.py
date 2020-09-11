
__all__ = []

# wkd
from ._repr import module


@module('wkd')
class Error(Exception):
    # base exception for all wkd errors
    
    def __init__(self, message):
        super().__init__(message)
        
    @property
    def message(self):
        return self.args[0]

        
@module('wkd')
class UsageError(Error):
    # exception indicating that the user has misused the wkd API in some way
    pass

    
@module('wkd')
class AlreadyOpenedError(UsageError):
    # raised when a resource that must be opened or closed is attempted to be
    # opened when it is already opened
    pass

    
@module('wkd')
class NotOpenedError(UsageError):
    # raised when a resource that must be opened or closed is asked to perform
    # an operation that requires it to be opened, but it is not opened
    pass
