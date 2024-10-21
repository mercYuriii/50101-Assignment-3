# Problem 2
#
# Yuri Carreira Alflen

# Take an input
test = input("Enter a string, and we will determine whether your input is a number: ")

def is_number(astring):
# Test whether a string is a number. By number we are referring to any rational number that is either in integer form or decimal form.
# Conditions that must be met for the string to be a number:
    # After removing trailing and leading spaces, a string can be converted into a number if there are no non integer characters other than ".".
    # If there is a "-" in the string, it must be the first non-space character
    # If there is a ".", then there can only be one instance of that character
    # "." can be anywhere in the string as long as it does not violate one of the previous conditions.

    # remove trailing spaces
    trim_astring = astring.strip()

    # Check if string contains a "-"
    if "-" in trim_astring:
        # If it is not in the correct position then it cannot be a number
        if trim_astring.find('-') != 0:
            # return False
            return False
        
    # remove a single instance of "." if it exists
    onlyints = trim_astring.replace('.','',1)
    
    # if number
    try:
        int(onlyints)
        
        # return True
        return True 
    
    # else:
    except:

        # return False
        return False
    
print(is_number(test))
