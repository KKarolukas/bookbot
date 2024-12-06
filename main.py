#read frankenstein file 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    number_of_chars = calculate_chars(text)
    print(number_of_chars)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()   

def calculate_chars(text):
    storage = {}
    for letter in text.lower():
        if letter in storage:
            storage[letter] += 1
        else:
            storage[letter] = 1
    
    return storage
    #return lower_case_text


if __name__ == "__main__":
    main()