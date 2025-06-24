from logger import logging

def add(a,b):
    logging.debug("add takes place")
    return a+b
logging.debug("func called")
add(1,2)
    
