from collections import Counter


mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]


print(Counter(mylist))


sentence = "How ,many times does each word show up in this sentence with a word"
print(Counter(sentence.split()))




letters = 'aaaaaabbbbbcccdddddddddd'


c = Counter(letters)
print(c.most_common())

