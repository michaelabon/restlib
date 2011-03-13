from MockHTTPResponse import MockHTTPResponse

class MockHTTPConnection:
    def __init__(self, responses):
        self.responses = responses

    def request(self, method, url,body=None, headers=None,):
        if method == "GET":
            self.response = MockHTTPResponse(responses.GET[url][0])

    def getresponse(self):
        return response

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
