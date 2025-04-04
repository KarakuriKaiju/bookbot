from stats import get_num_words
from stats import get_num_char

# Takes a file path as an input and returns the contents of the file as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


book_text = get_book_text("books/frankenstein.txt")
word_count = get_num_words(book_text)
char_count = get_num_char(book_text)

print(char_count)