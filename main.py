"""
inputs: ("9238372", ["minou", "michelle", "carl", ...]
output: ["minou", "michelle"]
description: find the words that can be associated with certain telephone numbers
1: nothing
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
0: nothing
"""
# Create the dictionary.
number_to_letters = {
    '1': '-',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': '-'
}
def words_to_numbers(word):
    number = ' '
    for letter in word:
        for key, value in number_to_letters.items():
            if letter.lower() in value:
                number += key
    return number
new_word= input("Try a new word: ")
result = words_to_numbers(new_word)
print(f"The word '{new_word}' is the number: {result}")


#def find_words(number_as_string, array_of_words_as_string):
#result =  find_words("120746582", ["allo", "bye", "jesus", "madonna", "croquettes"])