#json.01.py
"""
The json module provides an API similar to pickle for converting in-memory Python objects to a serialized representation known as JavaScript Object Notation (JSON). Unlike pickle, JSON has the benefit of having implementations in many languages (especially JavaScript), making it suitable for inter-application communication. JSON is probably most widely used for communicating between the web server and client in an AJAX application, but is not limited to that problem domain.
"""
import json

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print('DATA:', repr(data))

data_string = json.dumps(data)
print('JSON:', data_string)

