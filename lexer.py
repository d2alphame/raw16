def ReadComment(StringToRead, Index):
    # this is for reading comments

    AChar = StringToRead[Index]             # Read the first character
    if AChar == "!":                        # Read the first exclamation mark
        Index += 1                          # Increment next index to read from

        AChar = StringToRead[Index]          # Read the next character
        if AChar == "!":                     # Read the second exclamation mark
            Index += 1                       # Always increment this after reading a valid comment character

            while AChar != "\n" and AChar != "\r":       # Keep reading until we get to a Cr or Lf
                AChar = StringToRead[Index]              # Read the next character fromt the string
                Index += 1                               # Increment this for each character in the comment that we read

            Index += 1                                   # Rememeber to increment the index after reading the entire comment

            return True                                  # Return True if we read a comment

        return False                       # This means we didn't detect a second "!" character

    return False                           # We didn't even detect the first "!" character


def ReadString(StringToRead, Index):
    # this is for reading strings begins and ends "
    return

def ReadHexadecimal(StringToRead, Index):
    # this reads an hexadecimal number
    return

def ReadDecimal(StringToRead, Index):
    # this reads a decimal number
    return

def ReadMacroDefinition(StringToRead, Index):
    # this reads a macro definition
    return

def ReadMacroInclude(StringToRead, Index):
    # this reads a macro inclusion
    return

def FileInclude(StringToRead, Index):
    # this reads a file inclusion 
    return