# Problem 3
#
# Yuri Carreira Alflen

test = 'Experience is the teacher of all things.'

def caesar_encrypt(key, message):
    # encrypt message using Caesar Cipher

    # start with all letters in the alphabet
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Build cipher alphabet based on key shift
    # To build cipher, slice the string at the key shift. Move the latter half to the begginning and the beggining to end
    cipher = base[key:] + base[:key]

    # prepare output for the loop to add to
    out = ''

    # convert letters from base alphabet to cipher alphabet
    # loop through characters in the message
    for character in message:
        #if character is not a letter, it won't be converted
        if character.isalpha():
            # check if letter is upper or lowercase
            if character.isupper():
                upper = 1
            else:
                upper = 0
            # find letter position in the base key. Force it to be uppercase regardless of casing to ensure it is converted by cipher
            position = base.find(character.upper())
            # convert it to cipher letter by using the base key position in the cipher and add it to the encypted output while maintaining casing
            if upper == 0:
                out += cipher[position].lower()
            else:
                out += cipher[position]
        else:
            out += character

    # return encryption
    return(out)


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

    # return decryption
    return(out)

a = caesar_encrypt(12,test)

# print encryption
print(a)

#print decryption
print(caesar_decrypt(12,a))