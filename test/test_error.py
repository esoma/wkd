
def test_error():
    from wkd import Error
    assert(issubclass(Error, Exception))
    
    error = Error('message')
    assert(error.message == 'message')
    
    
def test_usage_error():
    from wkd import Error, UsageError
    assert(issubclass(UsageError, Error))
    
    error = UsageError('message')
    assert(error.message == 'message')
    
    
def test_already_opened_error():
    from wkd import UsageError, AlreadyOpenedError
    assert(issubclass(AlreadyOpenedError, UsageError))
    
    error = AlreadyOpenedError('message')
    assert(error.message == 'message')
    
    
def test_not_opened_error():
    from wkd import UsageError, NotOpenedError
    assert(issubclass(NotOpenedError, UsageError))
    
    error = NotOpenedError('message')
    assert(error.message == 'message')
