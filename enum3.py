class Dict(dict):
    def __init__(self):
        self.count = 0

    def __getitem__(self, key):
        if key.startswith('__') and key.endswith('__'):
            return super().__getitem__(key)

        self[key] = self.count
        self.count += 1


class Type(type):
    def __prepare__(*args):
        return Dict()


class Enum(metaclass=Type):
    ...
