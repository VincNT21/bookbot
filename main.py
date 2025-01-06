def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    characters_dict = count_characters(text)
    print(characters_dict)


def get_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
        words = text.split()
        return len (words)


def count_characters(text):
    char_dict = {}
    for char in text:
        low_char = char.lower()
        if low_char not in char_dict:
             char_dict[low_char] = 1
        else:
             char_dict[low_char] += 1
    return char_dict


main()
