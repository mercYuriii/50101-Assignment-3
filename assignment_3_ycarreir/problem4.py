# Problem 4
#
# Yuri Carreira Alflen

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
        string_list = file.read().split()


    
    # Return an error if file does not exist
    except FileNotFoundError:
        print("File does not exist")
    
    # sort list
    sorted_items = sorted(string_list)

   # Return a tuple
    return filename, sorted_items, number_of_lines

# Snippet to run function
(filename, items, lines) = process_file("common_words.txt")