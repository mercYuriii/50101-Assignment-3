# Problem 9
#
# Yuri Carreira Alflen

# Load the common words list leveraging problem 4
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

        #print(string_list) - TEST
    
    # Return an error if file does not exist
    except FileNotFoundError:
        print("File does not exist")
    
    # sort list
    sorted_items = sorted(string_list)

   # Return a tuple
    return filename, sorted_items, number_of_lines

# Snippet to run function
(filename, common_items, lines) = process_file("common_words.txt")

# add speech file
speechfile = open("speech.txt","r")
speech = speechfile.read()

# clean up speech for analysis. (same casing and remove punctutation)
speech = speech.lower()

# list punctuation to remove
punctuation = ['.','?','!',';',':', ',']
for pos in range(len(punctuation)):
    speech = speech.replace(punctuation[pos], ' ')

#print(speech) - TEST

# split speech in list of words
speech_list = speech.split()
#print(speech_list) - TEST

# remove all words that are in the common list
# create new list for uncommon words
unique_list = []
unique_counter = []

# loop through speech to find unique words and count those unique words
for word in speech_list:
    if word not in common_items:
        if word not in unique_list:
            unique_list.append(word)
            unique_counter.append(1)
        else:
            position = unique_list.index(word)
            unique_counter[position] += 1

#print(unique_list)
#print(unique_counter)

# to find the 20 largest words, find the max in the counter, identify it's position in the list, enter that position in the list of words, and pop out both of those values from respective list. print result Repeat 20 times
for i in range(20):
    value = max(unique_counter)
    pos = unique_counter.index(value)
    word = unique_list[pos]
    print(word + ' - ' +str(value))
    unique_counter.pop(pos)
    unique_list.pop(pos)

