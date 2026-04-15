def get_num_words(text):
    words = text.split()
    return len(words)


def character_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:characters[char] = 1
    return characters


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    chars_dict = []
    for char in num_chars_dict:
        chars_dict.append({"char": char, "num": num_chars_dict[char]})
    chars_dict.sort(reverse=True, key=sort_on)
    return chars_dict
    