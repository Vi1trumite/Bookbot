import sys
from stats import get_num_words, character_count, chars_dict_to_sorted_list


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    char_count = character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)
    print_report(sys.argv[1], num_words, chars_sorted_list)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars_sorted_list:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()
