import sys
from stats import word_count
from stats import character_dic
from stats import sorted_char_dic
def get_book_text(p):
    with open(p) as f:
        content = f.read()
        return content
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        content = get_book_text(sys.argv[1])
        char_list = sorted_char_dic(character_dic(content))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(content)} total words")
        print("--------- Character Count -------")
        for character in char_list:
            print(f"{character['char']}: {character['num']}")
        print("============= END ===============")
main()
