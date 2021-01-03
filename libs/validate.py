
import json

# Validate different possible ways of Sessions concerning key's configurations 
# and Requests that can be presented by users

class Validate():
    def __init__(self):
        pass
        
    # interpret requests in it's possible formats
    # returns a json with requested data

    def read_requests(self, request):
        if (request.data.__len__() == 0):
            return request.args.to_dict(flat=True)
        else:
            return json.loads(request.data)