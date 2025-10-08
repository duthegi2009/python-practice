# String analyzer

# User Input
sentence = "" #Please write down the sentence you want between""

# String Length
length = len(sentence)

# The first letter. The last letter
first = sentence[0]
last = sentence[-1]

# uppercase, lowercase conversion
upper_case = sentence.upper()
lower_case = sentence.lower()

# Slicing
front_part = sentence[:3]
back_part = sentence[-3:]

# String Format
print("\n=== String Analysis Results ===")
print("Sentence length : " + str(length))
print("the first letter :" + first)
print("The last letter : " + last)
print("The first three letters :" + front_part)
print("The last three letters : " + back_part)

# String processing function
print("Convert to capital letters : " + upper_case)
print("Converting to lowercase : " + lower_case)

# Using Escape Characters
print("\n\t--- Ending Analysis ---\n")