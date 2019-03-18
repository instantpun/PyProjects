'''This module will call pyperclip and regex and search for specified strings.'''

import pyperclip
import re



def clear_clip():
	"This function clears the contents of the system clipboard when it is invoked."
	pyperclip.copy("")
	
	return pyperclip.paste()




def test_str_type(input):
	try:
		assert isinstance(input, str) is True, "Error: 'input' must be a string or a list of string characters."
	except AssertionError as e:
		print("{}".format(e))
		return False
	else:
		return True

def test_str_not_null(input):
	try:	
		assert input != "", "Error: 'input' cannot be an empty string." 
	except AssertionError as e:
		print("{}".format(e))
		return False
	else:
		return True

def test_string(input):
	
	if test_str_type(input) is False or test_str_not_null(input) is False:
		print("Error: Invalid input.\nExiting...")
		return False
	else:
		return input

# input_data = re.compile(pattern_src_ip, re.I)
# print("Compiled regex string:\n" + str(input_data))
# print("\n" + str(dir(input_data)) + "\n")


# regex pattern defintions:

pattern_dict = {
	'src_ip' : r'source\sip\s(?P<src_ip>(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))',
	'dst_ip' : r'destination\sip\s(?P<dst_ip>(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))'}

def return_regex():
	# verify if test_input() returned False on any of its checks
	if test_string(pyperclip.paste()) != False:
		print("First check passed\n")
		print("Copying data...\n")
		input_data = pyperclip.paste()
		src = 'src_ip'
		dst = 'dst_ip'
		try:
			print("Parsing data...\n")
			# create new dict and keep the same keys as pattern_dict. New values will be regex search objects based on item values in pattern_dict.
			re_dict = { k: re.search(v, input_data, re.I) for k, v in pattern_dict.items()}
			# if re.search() can't match the pattern given to a string inside input_data, it returns a NoneType object for that pattern
			# NoneType object will not have the group attribute
			assert hasattr(re_dict[src], 'group') is True, "Error: group attribute is missing from search object."
			'''IMPORTANT:
				This assert statement needs to be redone, perhaps using a loop.
				It does a poor job of checking for NoneType objects returned by re.search.
				Currently, it will only catch an exception, if 
				the object mapped to re_dict['src_ip'] is missing the group attribute.'''
		except AssertionError as e:
			print("{}\nSecond check failed.\nSearch string did not match any predefined patterns.\nExiting...".format(e))
		else:
			print('second check passed')
			print("\nThis is the list of compiled regex objects:\n {}".format(re_dict))
				
			try:
				print("\nHere's the regex matches we found: \n src {} \n dst {}".format(re_dict[src].group(src), re_dict[dst].group(dst)))
			except AttributeError as e:
				print("\nDoesn't seem like the regex search returned any matches. :(\n{0}\n".format(e))

	else:
		print('There was a problem with the clipboard input, please try again')


#clear_clip()
return_regex()

