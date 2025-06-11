def get_num_words(book):
    words = book.split()
    count = len(words)
    print(f"{count} words found in the document")