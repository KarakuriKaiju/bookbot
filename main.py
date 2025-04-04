import sys
from stats import get_num_words
from stats import get_num_char
from stats import sort_char


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print if the character is alphabetic
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

# Main execution
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]  # Get the path from command line
book_text = get_book_text(book_path)
word_count = get_num_words(book_text)
sorted_chars = sort_char(book_text)


# Print the report
print_report(book_path, word_count, sorted_chars)