DAY 21 - STRING METHODS

word = "Welcome"
print(word)
word = word.lower()
print(word)
word = word.upper()
print(word)
word = word.capitalize()
print(word)
print(" Welcome ".lstrip())
print(" Welcome ".rstrip())
print(" Welcome ".strip())
print(word.find("come"))
print(word.find("hello"))
print(word.count("come"))
print(word.count("hello"))
word = word.replace("Welcome", "hello world") 
print(word)
word = word.replace(" ", "")
print(word)

-- String operators.py
word1 = "hello"
word2 = 'hi'
print(word1)
print(word2)
print(word1 != word2)
print(word1 == word2)
word2 = "Hello"
print(word1)
print(word2)
print(word1 != word2)
print(word1 == word2)
word2 = "hello"
print(word1)
print(word2)
print(word1 == word2)
print(word1 != word2)
word2 = "world"
print(word1)
print(word2)
word3 = word1 + word2
print(word3)
word3 = word1 + " " + word2
print(word3)
word4 = 'h' * 5
print(word4)
word5 = "bye" * 3
print(word5)
print('e' in word1)
print('e' not in word1)
print('hi' in word2)
print('hi' not in word2)
