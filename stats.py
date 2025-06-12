def get_num_words(book):
    words = book.split()
    count = len(words)
    print(f"{count} words found in the document")

def get_char_count(book):
    words = book.lower()
    total = {}
    for char in words:
        if char in total:
            total[char] += 1
            continue
        else:
            total[char] = 1
    print(total)