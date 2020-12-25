from flask import session
from functools import wraps

def check_logged_in(func):
    #This is reusable with any of the 3 functions that display pages 1-3
    @wraps(func)
    def wrapper(*args, **kwargs):
        #The changes to the original functions are done here
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
    #The returned object after the changes
    #Now this decorator can be used by being called upon
    #right before invoking the function that needs changing
    #using the syntax: '@check_logged_in'