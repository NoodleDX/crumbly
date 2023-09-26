# ==========================================
#             Crumbly Library
#      The (useless probably) library
#  for giving something multiple variables
#               By NoodleDX
# ==========================================

# Check the README for the usage docs!
import json

class Crumb():
    '''A Crumb object.
    Usage: crumbname = Crumb(var=value, var2=value, var3=value, etc)'''
    
    def __init__(self, **kwargs):
        self.data = kwargs

    def __getattr__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(f"The key '{key}' does not exist in that Crumb")

    def __setattr__(self, key, value):
        if key == "data":
            super().__setattr__(key, value)
        else:
            self.data[key] = value

    def __delattr__(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(f"The key '{key}' does not exist in that Crumb")

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Crumb({self.data})"

    def __len__(self):
        return len(self.data)

    def keys(self):
        '''Lists all the keys in a Crumb.
        Usage: var =  crumbname.keys()'''
        return self.data.keys()

    def values(self):
        '''Lists all the values in a Crumb.
        Usage: var = crumbname.values()'''
        return self.data.values()

    def items(self):
        '''Lists all the items in a Crumb.
        Usage: var = crumbname.items()'''
        return self.data.items()

    def copy(self):
        '''Makes a clone of a Crumb.
        Usage: crumb2name = crumbname.copy()'''
        return Crumb(**self.data)

    def clear(self):
        '''Deletes every key in a Crumb.
        Usage: crumbname.clear()'''
        self.data.clear()

    def to_json(self):
        '''Turns a Crumb into JSON data.
        Usage: json_crumb = crumbname.to_json()'''
        return json.dumps(self.data)

    @classmethod
    def from_json(cls, json_string):
        '''Makes a Crumb out of JSON data.
        Usage: crumbname = Crumb.from_json('{"var": value, "var2": value, etc}')'''
        data = json.loads(json_string)
        return cls(**data)
