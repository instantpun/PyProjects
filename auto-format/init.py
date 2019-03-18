"""
UNDERSTANDING SELF AND __INIT__ METHOD IN PYTHON CLASS.
Before understanding the "self" and "__init__" methods in python class, it's very helpful if we have the idea of what is a class and object.

Class : 

Class is a set or category of things having some property or attribute in common and differentiated from others by kind, type, or quality.

In technical terms we can say that class is a blue print for individual objects with exact behaviour.

Object :

object is one of instances of the class. which can perform the functionalities which are defined in the class.

self :

self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.

__init__ :

"__init__" is a reserved method in python classes. It is known as a constructor in object oriented terms. This method is called when an object is created from a class and it allows the object to initialize the attributes of that class.
"""

import sys
sys.path.append(0, '/home/Gatekeeper/github/PyProjects/auto-format')
import pyperclip
import custom_regex

## may need to create an object for email messages, header, subject, body, etc
## creating a generic object for the email message to be used as data sources

class messageSource:
	def __init__(self, header = "", sHostIp = "0.0.0.0", sPort = 0, datetime = "", dHostIp = "0.0.0.0", dPort = 0, note = "", footer = ""):
		"This creates the attributes for the messageSource object"
		self.header = str(header)
		self.sHostIp = str(sHostIp)
		self.sPort = str(sPort)
		self.datetime = str(datetime)
		self.dHostIp = str(dHostIp)
		self.dPort = str(dPort)
		self.note = str(note)
		self.footer = str(footer)
		
	def get_header(self):
		"This returns the loosely defined header information of messageSource"
		return self.header
	
	def get_sHostIp(self):
		"This returns the source host IP information within the messageSource"
		return self.sHostIp
	
	def get_sPort(self):
		"This returns the source port information within the messageSource"
		return self.sPort
	
	def get_datetime(self):
		"This returns the timestamp/datetime information of the messageSource"
		return self.datetime
	
	def get_dHostIp(self):
		"This returns the destination host IP information within the messageSource"
		return self.dHostIp
	
	def get_dPort(self):
		"This returns the destination host within the messageSource"
		return self.dPort
	
	def get_note(self):
		"This returns the additional information or notes within the messageSource"
		return self.note
	
	def get_footer(self):
		"This returns the loosely defined footer of the messageSource"
		return self.footer

def validateInput(x=0):
	"This sanitizes the user input, and then returns the input argument passed to it"
	# some stuff here
	return x
	
print(validateInput())
print(messageSource.get_dHostIp())
