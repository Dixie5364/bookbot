def get_num_words(book):
    words = book.split()
    count = len(words)
    return count

def get_char_count(book):
    words = book.lower()
    total = {}
    for char in words:
        if char in total:
            total[char] += 1
            continue
        else:
            total[char] = 1
    return total

def sorted_chars(dict):
    sorts = []
    for character, count in dict.items():
        if character.isalpha():
            new_list = {"char": character, "num": count}
            sorts.append(new_list)
        else:
            continue
    sorts.sort(reverse=True, key=lambda dict: dict["num"])
    return sorts
