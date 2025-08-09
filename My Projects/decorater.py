
def get_sprinkles(func):
    def wrapper():
        print("*let's put some sprinkles*")
        func()
    return wrapper
    
def get_more_ice(func):
    def wrapper():
        print("*let's put some ice bro*")
        func()
    return wrapper

@ get_more_ice
def get_ice_cream():
    print("*this is your ice cream*")

get_ice_cream()
