class NotIntError(Exception):
    def __init__(self, message='This module only works with integers'):
        super().__init__(message)



# raise NotIntError()
raise NotIntError(2.4)