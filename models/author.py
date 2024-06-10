class Author:
    def __init__(self, id, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._id = id
        self._name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    @property
    def name(self):
        return self._name
    @property
    def id(self):
        return self._id
    @id.setter    
    def id(self, id):
        if not isinstance (id , int):
            raise   TypeError("id must be an integer")
        self._id = id