class MockHTTPResponse:
    def __init__(self, response=None, status=200, reason="OK", version=11):
        self.response = response
        self.status = status
        self.reason = reason
        self.version = version
        self.msg = None
                
    def read(self, amt=None):
        return self.response
    
    def getHeader(self, name, default=None):
        pass
    
    def getHeaders(self):
        pass
    
    def fileNo(self):
        pass
