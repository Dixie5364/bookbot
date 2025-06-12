import sys
from stats import get_num_words
from stats import get_char_count
from stats import sorted_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_title):
    with open(book_path) as b:
        book_contents = b.read()
    return book_contents

title = get_book_text(book_path)

char_count_dict = get_char_count(title)
sorted_list_of_chars = sorted_chars(char_count_dict)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}")
print("----------- Word Count ----------")
print(f"Found {get_num_words(title)} total words")
print("--------- Character Count -------")
for item in sorted_list_of_chars:
    count = item["num"]
    character = item["char"]
    print(f"{character}: {count}")
print("============= END ===============")