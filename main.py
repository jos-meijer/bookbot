import sys
from stats import get_num_words, get_count_char, get_sorted_char_list

# ---

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def main(book_path):
    book = get_book_text(book_path)
    print("Analyzing book...")

    # word count
    words = get_num_words(book)
    print(f"Found {words} total words")
    
    # char count
    chars = get_count_char(book)
    sorted_chars = get_sorted_char_list(chars)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

# arg checking
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
main(book_path)
