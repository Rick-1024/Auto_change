from Utile01 import Loginfo
from Utile01 import Buffer
import datetime
class Initiatives:
      BUFFER=None
      LOGINFO=None
      SIMPLE=None

      def __init__(self):
          pass

      def getlog(self):
          log = Loginfo.Loginfo.init(self)
          Initiatives.LOGINFO = log
          return Initiatives.LOGINFO
      def getbuff(self):
          buffer = Buffer.Buffer.ali(self)
          Initiatives.BUFFER = buffer
          return Initiatives.BUFFER


