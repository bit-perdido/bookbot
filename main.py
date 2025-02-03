def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_lc = get_lowercase_text(text)
    num_words = get_num_words(text)
    character_count = get_character_count(text_lc)

    get_report(character_count, num_words, book_path)
    


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


def get_report(chad, num_words, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letter in chad:
        if letter <= "z" and letter >= "a":
            print(f"The '{letter}' character was found {chad[letter]} times")
    print("--- End report ---")


main()