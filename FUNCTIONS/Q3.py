# 3. Count Word Frequency
# Problem: Write a program that counts the frequency of each word in a given text.
# Use a function count_words(text) to count how many times each word appears in the
# text.
# Input: A string of text
# Output: A dictionary where the keys are words and the values are their frequencies

# Jainam Shah

def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for i in range(0,len(words)):
        word_count[words[i]]=0
        for j in range(0,len(words)):
            if words[i]==words[j]:
                word_count[words[i]]+=1
    return word_count

sentence = input("Enter a Sentence : ")
print(count_words(sentence))