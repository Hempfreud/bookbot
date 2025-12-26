def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

from stats import total_words, character_count, sort_chars

def main():
    book = get_book_text("./books/frankenstein.txt")
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {total_words(book)} total words
--------- Character Count -------""")

main()