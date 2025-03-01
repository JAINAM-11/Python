# 8. Word Count in Sentence
# Problem: Write a function count_words(sentence) that counts how many words are in a
# sentence. Words are separated by spaces, and punctuation should not be
# considered part of the words.

# Jainam Shah

import string

def count_words(sentence):
    word_count=0
    for char in sentence:
        if char.isspace():
            word_count+=1
    return word_count+1

user_input = input("Enter a sentence: ")
print(count_words(user_input))
