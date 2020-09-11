
# python
import logging

def test():
    from wkd import log
    assert(isinstance(log, logging.Logger))
    assert(log.name == 'wkd')
