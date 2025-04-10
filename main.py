from stats import get_num_words
from stats import char_stats
from stats import sorted_dict
import sys

# def get_book_text(filepath):
#     with open(filepath) as f:
#         file_contents = f.read()
#         return file_contents


def main():
    # print(get_book_text("./books/frankenstein.txt"))
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    char_summary = char_stats(sys.argv[1])
    # print(char_summary)
    final_data = sorted_dict(char_summary)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(sys.argv[1])
    print("--------- Character Count -------")
    for chars in final_data:
        if chars["char"].isalpha():
            print(f"{chars['char']}: {chars['count']}")
    print("============= END ===============")




main()

