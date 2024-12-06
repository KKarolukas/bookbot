#read frankenstein file 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    number_of_chars = calculate_chars(text)
    #print(f"{num_words} words found in the document")
    report = reporting(number_of_chars,num_words)
    
def sort_on(char_dict):
    return char_dict["num"]

def reporting(number_of_chars,num_words):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    chars_list = []
    for char, count in number_of_chars.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            chars_list.append(char_dict)
    
    chars_list.sort(reverse=True,key=sort_on)
    #print(chars_list)
    
    for letter in chars_list:
        print(f"The '{letter['char']}' character was found {letter['num']} times")   
         
    print()
    print("--- End report ---")
    
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

def chars_report(book_path, number_of_chars):
    print(f"--- Begin report of{book_path} ---")
    for char, count in number_of_chars.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


if __name__ == "__main__":
    main()