def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    # Get the book text by calling get_book_text with the path
    book_text = get_book_text("books/frankenstein.txt")
    # Print the book text
    print(book_text)

main()