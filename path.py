from parameter import parameter, header, query
from body import Body

class Path:
    def __init__(self, spec):
        self._path = ""
        self._method = ""
        self._parames = []
        self._body = []
        self._responses = []
        self._spec= spec
    
    def path(self, path):
        self._path = path
    
    def methods(self, method):
        self._method = method
    
    def parameters(self, parameters):
        header_to_ignore = ["Content-Type", "Accept", "Authorization"]
        for param in parameters:
            if param["in"] == "path":
                res = parameter(param["name"], param["schema"])
                self._parames.append(res)
            elif param["in"] == "query":
                res = query(param["name"], param["schema"])
            elif param["in"] == "header" and param["name"] not in header_to_ignore:
                res= header(param["name"])
            elif param["in"] == "cookie":
                pass
                # Not implemented yet
            else:
                pass
    
    def body(self, body):
        req_body = Body(self._spec)
        req_body.process_body(body)
        self._body = req_body

    def responses(self, responses):
        self._responses = responses
    