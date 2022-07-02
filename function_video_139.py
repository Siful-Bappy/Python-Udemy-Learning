### video 140

# def multiply():
#     result = 10.5 * 5
#     return result

# answer = multiply()
# print(answer)

### video 141 Program flow when calling a function
### video 143 Debugging with parameters


# def multiply(x, y):
#     result = x * y
#     return result

# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

### video 144 Palindromes
# def is_palindrom(strings):
#     return strings[::-1].casefold() == strings.casefold()

# word = input("Please enter a word to check: ")
# if is_palindrom(word):
#     print("{} is a palindrom".format(word))
# else:
#     print("{} is not a palindrom".format(word))


### video 145 sentence challenge solution

def is_palindrom(strings):
    return strings[::-1].casefold() == strings.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrom(string)

sentence = input("Please enter a word to check: ")
if palindrome_sentence(sentence):
    print("{} is a palindrom".format(sentence))
else:
    print("{} is not a palindrom".format(sentence))