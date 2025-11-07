def character_dic(content):
    string = content.lower()
    characters = {}
    for c in string:
        if c.isalpha():
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
    return characters
def sorted_char_dic(char):
    list_of_char = []
    for c in char:
        list_of_char.append({"char": c, "num": char[c]})
    def sort_on(items):
        return items["num"]
    list_of_char.sort(reverse=True,key=sort_on)
    return list_of_char
def word_count(content):
    length_of_book = content.split()
    return len(length_of_book)
