
__all__ = ()


class module:
    # decorator for explicitly overriding the __module__ of the decorated class
    # or function
    
    def __init__(self, module_name):
        self.module_name = module_name
        
    def __call__(self, obj):
        obj.__module__ = self.module_name
        return obj
