import logging
#logging.basicConfig(level=logging.CRITICAL) # default is warnning
#logging.basicConfig(level=logging.DEBUG) # default is warnning
logging.basicConfig(level=logging.WARNING, filename='example.log', filemode='w', format='%(asctime)s    %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p') # default is warnning
logging.debug("This message will be ignored")
logging.info("This should be ignored")
logging.warning("And this, too")
