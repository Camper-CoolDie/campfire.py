import json
import base64
from io import BytesIO
from datetime import datetime, timedelta
from hashlib import sha512
from .reqs.request import create_request, RequestManager, FLAG_DATAOUTPUT

API_BOT_TOKEN = ''
API_LOGIN_TOKEN = ''

reqmgr = RequestManager()

def request(params, *flags, **kwargs):
    data = reqmgr.send(create_request(params, *flags, **kwargs))
    return json.loads(data)

def campreq(params, *flags, **kwargs):
    params["J_API_BOT_TOKEN"] = API_BOT_TOKEN
    params["J_API_LOGIN_TOKEN"] = API_LOGIN_TOKEN
    
    content = request(params, *flags, **kwargs)
    
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

def get_date(ms):
    return datetime.fromtimestamp(ms / 1000.0)

def get_resource(resource):
    if resource:
        if hasattr(resource, "read"):
            res = resource.read()
        else:
            with open(resource, "rb") as f:
                res = f.read()
    return res

def get_resources(resources):
    return [ get_resource(res) for res in resources ]

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