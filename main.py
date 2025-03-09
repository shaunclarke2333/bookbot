from stats import words_in_string
from stats import character_count
import sys


def get_book_text (file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():

    try:
        
        book_path = sys.argv[0:]
        # print(f"This is entries count {count_entries}")
        if len(book_path) < 2:
            print(f"Usage: python3 main.py <path_to_book>")
            return
        else:
            book_path = sys.argv[1]
            text = get_book_text(book_path)
        
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at books/{book_path}...")
        word_count = words_in_string(text)
        
        print(word_count)

        print(f"--------- Character Count -------")
        number_of_characters = character_count(text)

        print(number_of_characters)
    except Exception as e:
        print(e)

main()


