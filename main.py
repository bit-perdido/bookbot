def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_lc = get_lowercase_text(text)
    num_words = get_num_words(text)
    character_count = get_character_count(text_lc)

    print("Amount of each character in the text:")
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_character_count(text):
    counter = {}
    letter = ""
    for l in text:
        if l in counter:
            counter[l] += 1
        else:
            counter[l] = 1
    return counter


def get_lowercase_text(text):
    return text.lower()


def get_num_words(text):
    words = text.split()
    return len(words)


main()