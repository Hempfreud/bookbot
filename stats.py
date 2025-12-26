def total_words(file_content):
    words = file_content.split()
    words_count = len(words)
    return words_count

def character_count(file_content):
    file_content = file_content.lower()
    char_count = {}
    for c in file_content:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_chars(char_count):
    list_dict = []
    for char, count in char_count.items():
        new_dict = {"char": char, "num": count}
        list_dict.append(new_dict)
    def sort_on_num(dict):
        return dict["num"]
    list_dict.sort(reverse=True, key=sort_on_num)
    return list_dict