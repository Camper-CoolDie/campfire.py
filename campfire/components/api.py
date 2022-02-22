import urllib3
import json
import base64
from io import BytesIO
from datetime import datetime, timedelta
from hashlib import sha512

LINK_CAMPFIRE = 'https://campfiresayzen.net:4026'
CERT = "/".join(__spec__.origin.split("/")[:-1]) + "/cert.pem"

API_BOT_TOKEN = ''
API_LOGIN_TOKEN = ''

http = urllib3.PoolManager(ca_certs=CERT, cert_reqs='REQUIRED')

def request(link, params):
    response = http.urlopen('POST', LINK_CAMPFIRE, body = json.dumps(params).encode())
    return response

def campreq(params = None):
    params["J_API_BOT_TOKEN"] = API_BOT_TOKEN
    params["J_API_LOGIN_TOKEN"] = API_LOGIN_TOKEN
    
    response = request(LINK_CAMPFIRE, params)
    content = json.loads(response.data)
    
    if content["J_STATUS"] == "J_STATUS_ERROR":
        raise ApiError(content["J_RESPONSE"])
    else:
        return content["J_RESPONSE"]

class ApiError(Exception):
    def __init__(self, content):
        if len(content["params"]) > 0:
            text = "Exception occured -- %s (%s)" % (content["code"], content["params"])
        else:
            text = "Exception occured -- " + content["code"]
        
        self.code = (content["code"], content["messageError"], content["params"])
        
        super(ApiError, self).__init__(text)

def auth(email, password, bot_token = ""):
    if bot_token != "":
        global API_BOT_TOKEN
        API_BOT_TOKEN = bot_token
    
    global API_LOGIN_TOKEN
    API_LOGIN_TOKEN = "Email - %s - %s" % (email, sha512(password.encode()).hexdigest())

def get_resource(resource):
    if hasattr(resource, "read"):
        res = base64.b64encode(resource.read()).decode("ascii")
    else:
        with open(resource, "rb") as f:
            res = base64.b64encode(f.read()).decode("ascii")
    return res

def get_resources(resources):
    res = []
    for resource in resources:
        if hasattr(resource, "read"):
            res.append(base64.b64encode(resource.read()).decode("ascii"))
        else:
            with open(resource, "rb") as f:
                res.append(base64.b64encode(f.read()).decode("ascii"))
    return res

def get_date(ms):
    return datetime.fromtimestamp(ms / 1000.0)

def get_timestamp(data):
    if isinstance(data, datetime):
        return int(data.timestamp() * 1000.0)
    else:
        return int(data)

def get_deltastamp(data):
    if isinstance(data, timedelta):
        return int(data.total_seconds()) * 1000 + int(data.microseconds / 1000)
    else:
        return int(data)