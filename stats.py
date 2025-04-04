#file used to refactor functions


def get_num_words(text):
    #splits the words in the file
    word_count = text.split()
    #Using len, counts the numbers of words in the document
    return len(word_count)

def get_num_char(text):
     #convert text to lowercase and to avoid duplicates
    text_lower = text.lower()
    char_count = {}
     #Iterate through each character in the text
    for char in text_lower:
          #if character is in the dictionary already, then add 1
        if char in char_count:
            char_count[char] += 1
          #else add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1
    return char_count 

def sort_char(text):
    # Get the dictionary of characters and their counts
    char_dict = get_num_char(text)
    
    # Create a list of dictionaries
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    # Define a helper function for sorting
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list from greatest to least by count
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
