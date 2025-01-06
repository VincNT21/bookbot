def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    characters_dict = count_characters(text)
    list_dict = dict_to_list(characters_dict)
    sorted_list = order_dict(list_dict)
    alpha_list = filter_alpha(sorted_list)
    make_report(book_path, num_words, alpha_list)    


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


def dict_to_list(dict):
    list = []
    for k in dict:
        list.append({"char": k, "num": dict[k]})
    return list


def sort_on(dict):
    return dict["num"]


def order_dict(list_dict):
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict


def filter_alpha(sorted_list):
    return [item for item in sorted_list if item["char"].isalpha()]



def make_report(book_path, num_words, ordered_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for c in ordered_dict:
        print(f"The '{c["char"]}' character was found {c["num"]} times")
    print("--- End report---")

     
main()
