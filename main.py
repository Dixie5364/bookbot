def get_book_text(book_title):
    with open(f"./books/{book_title}") as b:
        book_contents = b.read()
    return book_contents

from stats import get_num_words

title = get_book_text("frankenstein.txt")

from stats import get_char_count

get_num_words(title)

get_char_count(title)