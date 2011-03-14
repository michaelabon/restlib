from MockHTTPResponse import MockHTTPResponse
import urlparse

class MockHTTPConnection:
    def __init__(self, responses):
        self.responses = responses

    def request(self, method, url,body=None, headers=None,):
        split = urlparse.urlparse(url)
        path = split.path
        query = split.query
        if query:
            path = path + "?" + query
        if method == "GET":
            try:
                if path == "/400":
                    self.response = MockHTTPResponse(response = '{"exception":"Bad request"}', status=400, reason="Bad Request")
                elif path == "/403":
                    self.response = MockHTTPResponse(response = '{"exception":"Forbidden"}', status=403, reason="Forbidden")
                else:
                    self.response = MockHTTPResponse(self.responses.GET[path][0])
            except KeyError:
                self.response = MockHTTPResponse(response='{"exception":"File not found"}', status=404, reason="Not Found")

    def getresponse(self):
        return self.response

    def set_debuglevel(self):
        pass

    def set_tunnel(self):
        pass

    def connect(self):
        pass

    def close(self):
        pass

    def putrequest(
        self,
        request,
        selector,
        skip_host=False,
        skip_accept_encoding=False,
        ):
        pass

    def putheader(self, header, argument):
        pass

    def endheaders(self):
        pass

    def send(self, data):
        pass
