class User:
    def __init__(self, name= 'Default'):
        self.name = name
    
    
    def __str__(self):
        return 'name: ' + self.name