# ==========================================
#             Crumbly Library
#      The (useless probably) library
#  for giving something multiple variables
#               By NoodleDX
# ==========================================
class Crumb():
    def __init__(self, **kwargs):
        self.data = kwargs
    
    def __getattr__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(f"'Crumb' object has no key '{key}'")
    
    def _setattr__(self, key, value):
        if key == "data":
            super().__setattr__(key, value)
        else:
            self.data[key] = value
    
    def __delattr__(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(f"'Crumb' object has no key '{key}'")
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Crumb({self.data})"

    def addData(self, key, value):
        self.data[key] = value
    
    def __len__(self):
        return len(self.data)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def copy(self):
        return Crumb(**self.data)

    def has_key(self, key):
        return key in self.data

    def clear(self):
        self.data.clear()

    def toDict(self):  # I'll be honest I don't know if this works or not cuz idk how to use my own library
        return self.data
    
    def makeJSON(self):
        import json
        return json.dumps(self.data)

    @classmethod
    def crumbFromJSON(cls, json_string):
        import json
        data = json.loads(json_string)
        return cls(**data)
