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

"__init__" is a reserved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
"""

## may need to create an object for email messages, header, subject, body, etc
## creating a generic object for the email data sources

class dataSource:
	def __init__(self, header, lhost, lport, datetime, rhost, rport, note, footer):
		self.header = str(header)
		self.lhost = str(lhost)
		self.lport = str(lport)
		self.datetime = str(datetime)
		self.rhost = str(rhost)
		self.rport = str(rport)
		self.note = str(note)
		self.footer = str(footer)
		
	def get_header(self):
		return self.header
	
	def get_lhost(self):
		return self.lhost
	
	def get_lport(self):
		return self.lhost
	
	def get_datetime(self):
		return self.datetime
	
	def get_rhost(self):
		return self.rhost
	
	def get_rport(self):
		return self.rport
	
	def get_note(self):
		return self.note
	
	def get_footer(self):
		return self.footer
		
	def get_core(self):
		core = "{0} \r\n{1}".format(self.lhost, self.lport)
		return core

testsrc = dataSource("some header", "10.10.10.10", "123", "2018-12-07 12:32:08 CDT/CST", "186.0.76.40", "8443", "***stuff", "some footer")
print("Local Host is {0} from DIR".format(testsrc.get_lhost()))
print("message core is \n{0}".format(testsrc.get_core()))