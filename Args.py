import json
class Args:
    ORURL = "http://10.66.11.59:7599/spl/search"
    TEST_URL = ""
    FO_URL = "https://10.0.90.121:443/api/v2/cmdb/firewall/address?"
    DIS_URL = None
    ORIDATA_PROTOCOL = None
    FO_PROTOCOL = None
    TOKEN_KEY_TYPE = None
    TOKEN_KEY = None
    FO_PORT = None
    ORIDATA_PORT = None
    FO_IP = None
    ORIDATA_IP = None
    FO_USER= None
    FO_PASSWORD= None
    FO_SUFFIX = None
    OR_SUFFIX = None
    ACCET_TYPE = None
    OURY_TYPE = None
    LOG_FILE_PATH = None
    FILE_SIZE_LOG = None
    FILE_LOG_COUNT = None
    TEST_LOCAL_PATH = None
    ENCODE =  None
    QUERY = "{\"spl\":\"index=\\\"event\\\" isnotnull(device_ip)|times earliest=\\\"-1d@d\\\" latest=\\\"now\\\"| stats count() by device_ip|table device_ip\"}"
    QUERY1 = None
    SPL_QUERY = None
    SET_REQUESTS_MONTH_P = None
    SET_REQUESTS_MONTH_G = None
    SET_REQUESTS_MONTH_PU = None
    SET_REQUESTS_MONTH_DELETE = None
    FO_DENY_SUFFIX = None

    def __init__(self):
        conf01 = None
        fileReader = None
        try:
            '''配置环境路径：/opt/For_os_Conf.txt'''
            with open("E:\资源文本\pythonProject2\For_os_Conf", "r") as reada:
                conf01 = reada.read().replace("\n","")
                print(conf01)
            jsonObject = json.loads(conf01)
            self.ORIDATA_PROTOCOL = jsonObject.get("ORIDATA_PROTOCOL")
            self.FO_PROTOCOL = jsonObject.get("FO_PROTOCOL")
            self.TEST_URL = jsonObject.get("TEST_URL")
            self.DIS_URL = jsonObject.get("DIS_URL")
            self.FO_IP = jsonObject.get("FO_IP")
            self.ORIDATA_IP = jsonObject.get("ORIDATA_IP")
            self.FO_USER = jsonObject.get("FO_USER")
            self.FO_PASSWORD = jsonObject.get("FO_PASSWORD")
            self.TOKEN_KEY_TYPE = jsonObject.get("TOKEN_KEY_TYPE")
            self.ACCET_TYPE = jsonObject.get("ACCET_TYPE")
            self.OURY_TYPE = jsonObject.get("QURY_TYPE")
            self.LOG_FILE_PATH = jsonObject.get("LOG_FILE_PATH")
            self.TEST_LOCAL_PATH = jsonObject.get("TEST_LOCAL_PATH")
            self.FILE_SIZE_LOG = jsonObject.get("FILE_SIZE")
            self.FILE_LOG_COUNT = jsonObject.get("FILE_LOG_COUNT")
            self.QUERY1 = jsonObject.get("SPL_QUERY")
            self.ENCODE = jsonObject.get("ENCODE")
            self.FO_PORT = jsonObject.get("FO_PORT")
            self.ORIDATA_PORT = jsonObject.get("ORIDATA_PORT")
            self.OR_SUFFIX = jsonObject.get("OR_SUFFIX")
            self.FO_SUFFIX = jsonObject.get("FO_SUFFIX")
            self.SPL_QUERY = jsonObject.get("SPL_QUERY")
            self.ORURL = f"{self.ORIDATA_PROTOCOL}://{self.ORIDATA_IP}:{self.ORIDATA_PORT}{self.OR_SUFFIX}"
            self.FO_URL = f"{self.FO_PROTOCOL}://{self.FO_IP}:{self.FO_PORT}{self.FO_SUFFIX}"
            self.SET_REQUESTS_MONTH_P = jsonObject.get("SET_REQUESTS_MONTH_P")
            self.SET_REQUESTS_MONTH_G = jsonObject.get("SET_REQUESTS_MONTH_G")
            self.SET_REQUESTS_MONTH_PU = jsonObject.get("SET_REQUESTS_MONTH_PU")
            self.SET_REQUESTS_MONTH_DELETE = jsonObject.get("SET_REQUESTS_MONTH_DELETE")
            self.TOKEN_KEY = jsonObject.get("TOKEN_KEY")
            self.TOKEN_KEY_TYPE = jsonObject.get("TOKEN_KEY_TYPE")
            self.FO_DENY_SUFFIX = jsonObject.get("FO_DENY_SUFFIX")
            self.DIS_URL = f"{self.FO_PROTOCOL}://{self.FO_IP}:{self.FO_PORT}{self.FO_DENY_SUFFIX}"
        except Exception as e:
            print(e)
