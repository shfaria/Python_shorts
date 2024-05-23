from logs import logger

n= 10
class LameExeption(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

try:
    n = 2/0
    logger.info("Hello World")
except Exception as e:
    logger.error("exception occurred", e,exc_info=True)

else:
    logger.info("Hello again")
finally:
    print("finally always runs whether or not error")

if n!=0:
    logger.error("n is not  0", exc_info=True)
    raise LameExeption("lame!", 10)

