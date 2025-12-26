import sys
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

from stats import total_words, character_count, sort_chars

def main():
    book = get_book_text(sys.argv[1])
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {total_words(book)} total words
--------- Character Count -------""")
    dicts = sort_chars(character_count(book))
    for d in dicts:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
main()