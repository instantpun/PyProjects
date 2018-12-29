## Python Practice
# String Methods

a  = None;

"""________________Substring Searching_________________"""
a  = "Cisco Switch";
# string.index()
a.index("i");
# output: 1
# found match starting at index [1]

# string.count()
a.count("i");
# output: 2
# found two matches totaling 2

# string.find()
a.find("sco");
# output: 2
# found matching starting at index [2]
a.find("xyz");
# output: -1
# -1 is returned because substring "xyz" does not exist
# with the string of elements

"""________________String Manipulation_______________"""

a.lower();
# output: 'cisco switch'
# only changes the output given, the original string is unchanged
a.upper();
# output: 'CISCO SWITCH'
# only changes the output given, the original string is unchanged

b  = "   Cisco Switch   ";
b.strip();
# output: 'Cisco Switch'
# .strip by default removes all leading and trailing whitespaces

c = "$$$Cisco$Switch$$$";
c.strip("$");
# output: 'Cisco Switch'
# .strip can take 1 character as an argument and will then strip any matching character

b.replace(" ", "");
# output: "CiscoSwitch"
# .replace takes 2 arguments
# 1st is the character substring being replaced
# 2nd is what the substring is being replaced with

d = "Cisco,Juniper,HP,Avaya,Nortel";
d.split(",");
# output: ['Cisco', 'Juniper', 'HP', 'Avaya', 'Nortel']
# Argument defines the delimiter between substrings within d
# output is put into a list (indicated by the square brackets)

# <arg>.join(var)
"_".join(a);
# output: 'C_i_s_c_o_ _S_w_i_t_c_h'
# the character token "_" will be joined/concatenated with each element in the string


"""___________________Boolean Substring Evaluation_____________________"""
a.startswith("C");
# output: True
# method evaluates first element in string against the argument given
a.startswith("c");
# output: False
# case sensitive evaluation
a.endswith("h");
# output: True

"""___________________String Operators_____________________"""
x = "Cisco"
y = " Switch"

x + y
# print output: 'Cisco Switch'

x * 3
# print output: 'CiscoCiscoCisco'

"o" in x
# output: True
# checks to see if the substring is within string x

"b" in x
# output: False

"b" not in x
# output: True
# negates the normally false case

"""___________________String Formatting_____________________"""
# For creating string templates
# Example
str = "Cisco mode: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
print(str)

# Using string formats
# each {n} corresponds to one of the arguments passed to the .format() method
# the position 0,1,2, etc can be reused or swapped freely.
str2 = "Cisco mode: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
print(str2)

# the position 0,1,2, etc can be reused or swapped freely.
str3 = "Cisco mode: {0}, {2} WAN slots, IOS {0}".format("2600XM", 2, 12.4)
print(str3)

