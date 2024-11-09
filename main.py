def main():
    book_path = "books/frankenstein.txt"
    # stores text string as a variable
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = lower_case(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")

    # loops through all the letter counts in the letter_count list
    for letter, count in letter_count.items():
        # checks if the letter is an actual letter (not a symbol)
        if letter.isalpha():
            # prints the letter count report
            print(f"The {letter} character was found {count} times")
   
    print("--- End Report ---")


def get_num_words(text):
    # splits up text string into indivudal words and stores as a variable
    words = text.split()
    # counts how many strings are in the words variable
    return len(words)


def get_book_text(path):
    # open book at the book path
    with open(path) as f:
        # reads text and returns as a string
        return f.read()
    
def lower_case (text):
    letter_count = {}
    # change text to all lower-case
    lowered_string = text.lower()
    # splits up text into individual letters
    letters_list = list(lowered_string)
    
    # loops through every letter in the string
    for letter in letters_list:
        # checks if each letter is already in the letter_count dictionary
        if letter in letter_count:
            # if the letter is already in the dictionary, increment its count
            letter_count[letter] += 1
        else:
            # if the letter is not aleady in the dictionary, count it once
            letter_count[letter] = 1
    return letter_count

main()
