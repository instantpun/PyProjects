"""
#!/usr/bin/env python
This is necessary in linux environments. You’ve probably seen these before.
These interpreter directives are also called shebangs in Unix jargon.
They tell the program loader which interpreter should execute the script.
Consult the almighty googles for more info
"""


# grab command line arguments using argparser module
import argparse
from os import getcwd
import sys

workingdir = getcwd()
sys.path.append(str(workingdir))
print(workingdir)

# step 1: create a parser
# this is basically a container to hold command-line arguments
# ArgumentParser returns an object which is stored in 'parser'
parser = argparse.ArgumentParser(description='Process some CLI arguments.',
                                 prog='Streamline')
# allow user to view version info
parser.add_argument('-V','--version',
                    action='version',
                    version=r'''Program: Project Streamline
                    Version: 1.1
                    Predecessor: 1.0''',
                    help='Display version control information',
                    )
parser.add_argument('-o','--output',
                    help="Output result to a file.",
                    action="store_true")
# establish mutually exclusive CLI arguments for -c and -f
# create exclusive_args parser object
exclusive_args1 = parser.add_mutually_exclusive_group(required=False)
# The ArgumentParser object will hold all the information necessary to parse the command line into Python data types.
exclusive_args1.add_argument('-c', '--clipboard',
                             action='store_true', # False by default, if --clipboard is not specified
                             help='Uses clipboard contents as the data source',
                             )
# type= can take any callable function that accepts a single string argument
# and returns the converted value
exclusive_args1.add_argument('-f', '--file',
                             default=False, # sets default unless --file is specified
                             help='Uses contents of the specified file as the data source',
                             )
# mutually exclusive groups for quiet vs verbose output
exclusive_args2 = parser.add_mutually_exclusive_group(required=False)

exclusive_args2.add_argument('-q','--quiet',
                             action='store_true',
                             help="prints minimal command output"
                             )
exclusive_args2.add_argument('-v','--verbose',
                             action='store_true',
                             help="prints verbose command output"
                             )

#def test_outfile(filename):
#	filename = str(filename)
#	print(filename)
#	if args.output:
#		with open("{0}.txt".format(filename), "a") as f:
#			f.write(str(result))


# print(args.output)

# default message if no arguments are provided
def default_msg():
    info = r'''
    For more information about usage of the _this_ command, please use the -h option.

    Example:
    _this_.py -h'''
    return info


if __name__ == '__main__':
    current_args = parser.parse_args()
    output = [current_args.clipboard, current_args.file]
    print(output)
    if current_args.verbose == True:
        print("\nThese are the current arguments in use by this command:\n",
              "Value of clipboard argument: " + str(current_args.clipboard) + "\n",
              "Value of file argument: " + str(current_args.file) + "\n",
              )
    else:
        print("\nclipboard= {0} \nfile path= {1}".format(current_args.clipboard, current_args.file))
