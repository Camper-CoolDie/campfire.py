import socket
import ssl
import json
import ratelimit

LINK_CAMPFIRE_HTTPS = ('46.254.16.245', 4026)
LINK_CAMPFIRE_HTTP = ('46.254.16.245', 4028)
CAMPFIRE_HTTPS_HOSTNAME = 'campfiresayzen.net'

CERT_DIR = "/".join(__spec__.origin.split("/")[:-3]) + "/cert.pem"

class RequestManager(object):
    def __init__(self):
        pass
    
    @ratelimit.limits(calls = 100, period = 60)
    def send(self, req):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations(CERT_DIR)
            sock = context.wrap_socket(s, server_hostname = CAMPFIRE_HTTPS_HOSTNAME)
        except OSError:
            raise OSError("campfire is launched in the interpreter.")
        
        sock.connect(LINK_CAMPFIRE_HTTPS)
        for send in req:
            sock.send(send)
        data = sock.recv(256)
        
        if not data:
            raise ConnectionError("Received an empty data")
        
        headers, extra = data.split(b'\r\n\r\n', 1)
        headers = headers.split(b'\n')[1:]
        resheaders = {}
        for header in headers:
            header = header.decode("ascii")
            key, value = header.split(': ', 1)
            resheaders[key] = value
        
        content_length = int(resheaders["Content-Length"])
        
        bodydata = extra
        while content_length - len(bodydata) > 0:
            bodydata += sock.recv(content_length - len(bodydata))
        
        sock.close()
        return bodydata

FLAG_DATAOUTPUT = 0
FLAG_RESOURCE_REQUIRED = 10
FLAG_RESOURCE_NO_REQUIRED = 11
FLAG_RESOURCE_REQUIRED_LIST = 12
FLAG_RESOURCE_LIST = 13

def create_request(params, *flags, **kwargs):
    sends = []
    
    if FLAG_DATAOUTPUT in flags:
        params["dataOutput"] = []
        resources = kwargs["resources"]
        for res in resources:
            res, flag = res
            if res:
                if flag == FLAG_RESOURCE_REQUIRED or flag == FLAG_RESOURCE_NO_REQUIRED:
                    if hasattr(res, "read"):
                        res = res.read()
                    else:
                        with open(res, "rb") as f:
                            res = f.read()
                    sends.append(res)
                    params["dataOutput"].append(len(res))
                    required = flag == FLAG_RESOURCE_REQUIRED
                
                elif flag == FLAG_RESOURCE_REQUIRED_LIST or flag == FLAG_RESOURCE_LIST:
                    required = flag == FLAG_RESOURCE_REQUIRED_LIST
                    if required:
                        if len(res) == 0:
                            raise ValueError("This resource is required")
                        else:
                            params["dataOutput"].append(None)
                    
                    for realres in res:
                        if hasattr(realres, "read"):
                            realres = realres.read()
                        else:
                            with open(realres, "rb") as f:
                                realres = f.read()
                        sends.append(realres)
                        params["dataOutput"].append(len(realres))
            else:
                if required:
                    raise ValueError("This resource is required")
                params["dataOutput"].append(None)
    
    body = json.dumps(params).encode("ascii")
    headers = (
        "POST / HTTP/1.1",
        "Content-Type: application/json",
        "Content-Length: " + str(len(body))
    )
    
    return (
        ("\n".join(headers) + "\r\n\r\n").encode("ascii"),
        body,
        *sends
    )