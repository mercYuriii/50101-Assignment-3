# Problem 5
#
# Yuri Carreira Alflen

# Leverage problem 3 and 4 to decrypt a message

# Givens:
# List of 1k common words
# Encrypted message
# Decrypted function when we know what key we want

# In order to solve the encryption, we need to know what key to enter
# We can assume key = 0, and loop through the decryption function until we get a sentence that makes sense
# To determine whether a sentence makes sense, the decrypted output should have english words
# We can leverage the list of common words by assuming that the encrypted message has some number of common words
# There may be some instances where the entire sentence does not only have common words,
# so we want to ensure we can solve the encryption while leveraging the least amount of common words necessary while still providing a correct output
# If the encryption has a one letter word, we should not anchor to that one letter since a key shift could still be incorrect (i.e., giving us an 'i' when we want an 'a')
# We are likely fine in assuming that if any encrypted word > 1 letter can be found in the common words list, the key used is likely correct
# If the decryption contains no words > 1 letter, we cannot solve this problem

# Load the list of common words from problem 4
def process_file(filename): 
    """Read, sort and return a file""" 
    # Remove leading and trailing spaces
    filename = filename.strip()

  
    # Ensure filename some .txt filename was inputted. this means there should be at least one initial character and '.txt' ends the string
    # If these conditions are not met, it fails
    if len(filename) < 5 and filename[-4:] != '.txt':
        print("Please input a file ending in '.txt'")
        quit()

    # Try to open the file to check if it exists
    try:
        file = open(filename,"r")

        # Count lines in file
        number_of_lines = len(file.readlines())

        # Allow file to be reread. After being read, cursor is at the end of file. Must be reset. Learned in https://stackoverflow.com/questions/3906137/why-cant-i-call-read-twice-on-an-open-file
        file.seek(0)

        # create a list with no spaces
        string_list = file.read().lower().split()


    
    # Return an error if file does not exist
    except FileNotFoundError:
        print("File does not exist")
    
    # sort list
    sorted_items = sorted(string_list)

   # Return a tuple
    return filename, sorted_items, number_of_lines

# Snippet to run function
(filename, items, lines) = process_file("common_words.txt")

# Load the decryption function from problem 3 and add the piece where that some encrypted word that is at least 2 characters long must match some word in the common lists else recursively call the function with a different key

def caesar_decrypt(key, message):
    # decrypt message using Caesar Cipher

    # start with all letters in the alphabet
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Build cipher alphabet based on key shift
    # To build cipher, slice the string at the key shift. Move the latter half to the begginning and the beggining to end
    cipher = base[key:] + base[:key]

    # prepare output for the loop to add to
    out = ''

    # convert letters from cipher alphabet to base alphabet
    # loop through characters in the message
    for character in message:
        #if character is not a letter, it won't be converted
        if character.isalpha():
            # check if letter is upper or lowercase
            if character.isupper():
                upper = 1
            else:
                upper = 0
            # find letter position in the cipher key. Force it to be uppercase regardless of casing to ensure it is converted by base
            position = cipher.find(character.upper())
            # convert it to base letter by using the base key position in the cipher and add it to the decypted output while maintaining casing
            if upper == 0:
                out += base[position].lower()
            else:
                out += base[position]
        else:
            out += character
            out = out.lower()

    # check if a word in this decryption is in the common list
    # make a list of all decrypted words
    out_list = out.split()
    
    # loop through words in the decryption
    for word in out_list:
        # check word length (based on logic above)
        if len(word) > 1:
            # check if word is in common words list
            if word in items:
                # return decryption
                return out, key
    
    # If the we have tried all keys (i.e, the entire alphabet shifted, we cannot solve this encryption)
    if key == 25:
        print('We cannot solve this encryption')
        quit()

    # try another key if the current key doesn't work
    return caesar_decrypt(key + 1, message)


decrypted, key = caesar_decrypt(0,'mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp')

print('The key is: ' + str(key))
print('The message is: ' + decrypted)
