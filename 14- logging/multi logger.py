import logging
logging.basicConfig(level=logging.DEBUG,filename="logs.log",filemode="w",format = "%(asctime)s- %(name)s-%(levelname)s -%(message)s",datefmt="%y-%m-%d")
log1 = logging.getLogger("mod 1")
log1.setLevel(logging.DEBUG)
def add(a,b):
    log1.debug("add is performed ")
    return a+b
def sub(a,b):
    log1.debug("sub is perform")
    return a-b
def mul(a,b):
    log1.debug("mul is performed ")
    return a+b
def divide(a,b):
    try:
        log1.debug("division is performed ")
        return a/b
    except ZeroDivisionError:
        log1.error("this is zero divion error")
add(10,20)
sub(10,20)
mul(10,20)
divide(3,0)
