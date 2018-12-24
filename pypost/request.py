### Builtins ###
import pprint
import urllib.request
import json

### Classes ###
class Request:
    def __init__(self, url, request_type = "GET", data = None, headers = None):
        self.url = url
        self.request_type = request_type
        if self.request_type == "POST":
            data = urllib.parse.urlencode(data)
            data = bytes(data, "ascii")
            self.data = data
            self._request = urllib.request.Request(self.url, self.data)
        else:
            self._request = urllib.request.Request(self.url)
        if headers:
            for header, val in headers.items():
                self._request.add_header(header, val)

    def fetch(self):
        resp = urllib.request.urlopen(self._request)
        self.response = resp.read().decode("ascii")
        try:
            self.response = json.loads(self.response)
        except:
            pass
        

    
