from .constants import FETCH_URL, UPDATE_URL

class Request:
    def __init__(self, data, url = "", request_type = ""):
        self.data = data
        self.url = url
        self.request_type = request_type

    def __eq__(self, other):
        return self.data == other.data and self.request_type == other.request_type

    def __hash__(self):
        return hash(('data', self.data, 'request_type', self.request_type))

    def is_fetch(self):
        if self.request_type == "FETCH":
            return True
        else:
            return False

    def is_update(self):
        if self.request_type == "UPDATE":
            return True
        else:
            return False

    def set_type(self, type_val):
        self.request_type = type_val

        if self.request_type == "FETCH":
            self.url = FETCH_URL
        elif self.request_type == "UPDATE":
            self.url = UPDATE_URL

    def set_fetch_type(self):
        self.request_type = "FETCH"
        self.url = FETCH_URL

    def set_update_type(self):
        self.request_type = "UPDATE"
        self.url = UPDATE_URL 




class Response:
    def __init__(self, id, data, url, status, request_type):
        self.id = id
        self.data = data
        self.url = url
        self.status = status
        self.request_type = request_type
 
    def is_matching_request(self, obj):
        if self.id == obj.data and self.request_type == obj.request_type:
            return True
        else:
            return False


    def is_fetch(self):
        if self.request_type == "FETCH":
            return True
        else:
            return False

    
    def is_success(self):
        if self.status == "SUCCESS":
            return True
        else:
            return False


class StoreResponse:
    def __init__(self, sample_id, req_type, pos, exists):
        self.sample_id = sample_id
        self.req_type = req_type
        self.pos = pos
        self.exists = exists

    def does_id_exist(self):
        return self.exists



class Debugger:
    def __init__(self, enable):
        self.enable = enable

    def debug(self, message):
        if self.enable:
            print(message)

    def output(self, op_message):
        print(">> {}".format(op_message))