class WrongFields(Exception):
    def __init__(self, message=None, status_code=404) -> None:
        
        if not message:
            self.message = "Wrong email and name type"
        else:
            self.message = message
        
        self.status_code = status_code

class WrongEmailField(Exception):
    def __init__(self, message=None, status_code=404) -> None:
        
        if not message:
            self.message = "Wrong email type"
        else:
            self.message = message
        
        self.status_code = status_code

class WrongNameField(Exception):
    def __init__(self, message=None, status_code=404) -> None:
        
        if not message:
            self.message = "Wrong name type"
        else:
            self.message = message
        
        self.status_code = status_code

class EmailAlreadyExists(Exception):
    def __init__(self, message=None, status_code=409) -> None:
        
        if not message:
            self.message = "This email is already registered"
        else:
            self.message = message
        
        self.status_code = status_code