import sys
from STT.exceptions import STTException
from STT.logger import logging

logging.info("it is a test info")


try:
    print("hi")
except Exception as e:
    raise STTException(e, sys)