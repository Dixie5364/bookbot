def get_book_text(book_title):
    with open(f"./books/{book_title}") as b:
        book_contents = b.read()
    return book_contents

from stats import get_num_words

title = get_book_text("frankenstein.txt")

from stats import get_char_count

from stats import sorted_chars

char_count_dict = get_char_count(title)
sorted_list_of_chars = sorted_chars(char_count_dict)


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(title)} total words")
print("--------- Character Count -------")
for item in sorted_list_of_chars:
    count = item["num"]
    character = item["char"]
    print(f"{character}: {count}")
print("============= END ===============")