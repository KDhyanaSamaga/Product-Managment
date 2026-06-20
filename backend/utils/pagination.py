"""
This is for pagination i am trying to implement off set  based pagination
use this formula offset = (page-1)*limit
since this is a static website 
"""

def pagination(page,limit):
    offset = (page-1)*limit
    return offset
    