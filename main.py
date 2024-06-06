def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path).lower()
    num_words = get_num_words(text)
    print(num_words)

def get_text(book):
    with open(book) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words) 

main()