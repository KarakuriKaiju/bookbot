# Takes a file path as an input and returns the contents of the file as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    # Get the book text by calling get_book_text with the path
    book_text = get_book_text("books/frankenstein.txt")
    word_count = book_text.split()
    print(f"{len(word_count)} words found in the document")

main()