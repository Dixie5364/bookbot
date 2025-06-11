def get_book_text(book_title):
    with open(f"./books/{book_title}") as b:
        book_contents = b.read()
    return book_contents

def main():
    book = get_book_text("frankenstein.txt")
    words = book.split()
    count = len(words)
    print(f"{count} words found in the document")

main()