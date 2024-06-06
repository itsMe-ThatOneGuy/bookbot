def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path).lower()
    num_words = get_num_words(text)
    letter_dic = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,}
    text_count_dic = get_letter_count(letter_dic, text)
    text_count_list = convert_dic_to_list(text_count_dic)
    get_report(book_path, num_words, text_count_list)

def get_text(book):
    with open(book) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words) 

def get_letter_count(dic, text):
    dic_copy = dic
    for letter in dic:
        dic_copy[letter] = text.count(letter)
    return dic_copy

def sort_on(dic):
    return dic["num"] 

def convert_dic_to_list(dic):
    list = []
    for item in dic:
        list.append({"char":item, "num": dic[item]})
    list.sort(reverse=True, key=sort_on)
    return list

def get_report(path, num, list):
    print(f"--- Begin report of {path} ---")
    print(f"{num} words in the document")
    for item in list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

main()