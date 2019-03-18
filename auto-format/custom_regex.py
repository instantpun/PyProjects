## testbed for email source manipulation
import re

# define regex to parse data source

#def some_func

# match("HOST") from any string token inside

dataSource = "";

# identify if UT or MS-ISAC
regex1 = "U.T. SYSTEM.\n"

# open file or get from clipboard``
# options to add maybe?

# dataTokens = dataSource.split("\r\n")

# create binary search tree to iterate through dataTokens

src_ip = "source\sip\s(?<src_ip>(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))"

def test(x):
	if regex1 in x is True:
		return("do something")
	else:
		return("do something")


####################3
#
#	def get_core(self):
#		core = "{0} \r\n{1}".format(self.lhost, self.lport)
#		return core

# testsrc = dataSource("some header", "10.10.10.10", "123", "2018-12-07 12:32:08 CDT/CST", "186.0.76.40", "8443", "***stuff", "some footer")
# print("Local Host is {0} from DIR".format(testsrc.get_lhost()))
# print("message core is \n{0}".format(testsrc.get_core()))
