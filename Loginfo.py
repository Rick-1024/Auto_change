import logging
from logging.handlers import RotatingFileHandler
from Utile01 import Args
class Loginfo:
    def init(self):
        args =Args.Args()
        log = logging.getLogger("Runtime_log")
        log.setLevel(logging.DEBUG)
        file_hadne = logging.FileHandler("E:\资源文本\pythonProject2\yy")
        file_hadne.setLevel(logging.DEBUG)
        Stream = logging.StreamHandler()
        Stream.setLevel(logging.DEBUG)
        format = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
        file_hadne.setFormatter(format)
        Stream.setFormatter(format)
        log.addHandler(file_hadne)
        log.addHandler(Stream)
        '''
        logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",datefmt="%m-%d %H:%M",handlers=[logging.FileHandler("E:\资源文本\pythonProject2\yy","a","utf-8")])
        aa = logging.handlers.RotatingFileHandler(filename=args.TEST_LOCAL_PATH,maxBytes=args.FILE_SIZE_LOG,backupCount=args.FILE_LOG_COUNT,delay=False)
        log = logging.getLogger("Runtime_log")
        log.addHandler(aa)
        '''
        return log


