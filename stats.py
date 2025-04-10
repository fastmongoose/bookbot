def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_List = file_contents.split()
        num_words = len(word_List)
        print(f"Found {num_words} total words") 

def char_stats(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_List = file_contents.lower()
        word_summary = {}
        for char in word_List:
            if (char not in word_summary):
                word_summary[char] = 1
            else:
                word_summary[char] += 1
    return word_summary

def sorted_dict(dict):
    sorted_dict_list = []
    for char in dict:
        char_dict = {}
        char_dict["char"] = char
        char_dict["count"] = dict[char]
        sorted_dict_list.append(char_dict)
    sorted_dict_list.sort(key=lambda character: character["count"], reverse=True)
    return sorted_dict_list