def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
print("Number of words:", count_words(sentence))