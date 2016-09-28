#! /usr/bin/python

# The Imports
import sys
import os.path
import lexer

# Check if an argument was even passed to this script.
# Remember that sys.argv[0] is the name of this script itself.

if len(sys.argv) < 2:
# If a filename was NOT passed to this script...

    # Let the user know about it and then stop the script
    print "\nSpecify the name of a file whenever you run this script"
    print "Exiting...\n"
    exit()

else:
# If a filename was passed to the script...

    # Get the name of the file we want to 'Hex-compile'. This is passed as the
    # second arguemnt to this script
    FileName = sys.argv[1]

    # Check if the file exists
    if not os.path.isfile(FileName):

        # If it doesn't, let the user know and exit
        print ("\nThe file " + FileName + " does not exist")
        print "Exiting...\n"
        exit()

InputFile = open(FileName, 'r')     # Open the file for reading

# The codes for our tokens

GotComment = 0                      # Comment
GotHexaDecimal = 1                  # Hexadecimal Number
GotDecimal = 2                      # Decimal Number
GotString = 3                       # Raw String
GotMacroNameDefinition = 4          # Macro name when defining a Macro
GotMacroDefinition = 5              # Macro definition
GotEndMacroDefinition = 6           # End of Macro definition
GotMacroInclusion = 7               # Including a defined macro inline
GotFileInclusion = 8                # Including a file inline
GotWhitespace = 9                   # White space like space and tab
ReadingMacroDefinition = False		# Set to True while reading a Macro definition

FileContent = InputFile.read()      # Read the content of the file

C = lexer.ReadComment(FileContent, 0)
print C

#for Character in FileContent:
    #if Character == "!":
        
#def ReadComment():
    # Reads a comment. A comment begins with "!" and runs till the end of the
    # line

#def ReadHexadecimal():
    # Reads an Hexadecimal number. An hexadecimal number begins with "#" and is
    # followed by 2 hexadecimal characters. The hexadecimal characters are
    # a-zA-z0-9

#def ReadDecimal():
	# Reads a Decimal number. A Decimal number is a maximum of 3 digits.

#def ReadString():
	# Reads a string. A string begins and ends with the Double Quote

#def ReadMacroDefinition():
	# Reads a Macro Definiton