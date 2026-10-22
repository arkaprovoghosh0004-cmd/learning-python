from collections import Counter

para = input("Enter a paragraph or sentence: ")
listofwords = para.split()
noofwords = print("Total words: ",len(listofwords))

unique = len(set(listofwords))
print("Number of unique words: ", unique)

count = Counter(listofwords)
word, freq = count.most_common(1)[0]

print("Most common word: ", word, "appeared", freq, "times.")
