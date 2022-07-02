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

# def is_palindrom(strings):
#     return strings[::-1].casefold() == strings.casefold()

# def palindrome_sentence(sentence):
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     return is_palindrom(string)

# sentence = input("Please enter a word to check: ")
# if palindrome_sentence(sentence):
#     print("{} is a palindrom".format(sentence))
# else:
#     print("{} is not a palindrom".format(sentence))


### video 151 Functions that perfom actions means it not return anything
# def banner_text(text):
#     screen_width = 80
#     if len(text) > screen_width - 4:
#         print("EED!!")
#         print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
    
#     if text == "*":
#         print("*" * screen_width)
#     else:
#         output_string = "**{0}**".format(text.center(screen_width - 4))
#         print(output_string)

# banner_text("*")
# banner_text("Always look on the bright side of life...")
# banner_text("If lfe seems jolly rotten,")
# banner_text("There's something you've forgotten!")
# banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
# banner_text("When you're felling in the dumps,")
# banner_text("Don't be silly chumps")
# banner_text("Just purse your lips and whistle - that's the thing!")
# banner_text("And... always look on the bright side of life...")
# banner_text("*")


### video 152 handling invalid argument
### video 154 default parameters values 
### video 157 writing a docstring
### documention of build in exception https://docs.python.org/3/library/exceptions.html

# def banner_text(text, screen_width=50):
#     """
#     Get an integerfrom stardard input ()
    
#     the print `str` value 

#     :param text - The text should be string
#            screen_width - here used 50 however user can specifid the value
#     :return: The function wouldn't return anything
#     """

#     if len(text) > screen_width - 4:
#         raise ValueError("String {0} is larger then specifid width {1}".format(text, screen_width))
    
#     if text == "*":
#         print("*" * screen_width)
#     else:
#         output_string = "**{0}**".format(text.center(screen_width - 4))
#         print(output_string)

### way to display doc string or default doc string
# print(input.__doc__)
# print("*" * 80)
# print(banner_text.__doc__)

### another way to display doc string or default doc string 
# help(banner_text)

# banner_text("*")
# banner_text("Always look on the bright side of life...")
# banner_text("If lfe seems jolly rotten,")
# banner_text("There's something you've forgotten!")
# banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
# banner_text("When you're felling in the dumps,")
# banner_text("Don't be silly chumps")
# banner_text("Just purse your lips and whistle - that's the thing!")
# banner_text("And... always look on the bright side of life...")
# banner_text("*")


### video 160 Fibonacci numbers
### video 161 Wringt a Fibonacci function
### documentation for  economy of exception https://devguide.python.org/documenting/#economy-of-expression

def fibonacci(n):
    """Returns] the `n`-th Fibonacci number, for prositive `n`."""

    if 0 <= n <= 1:
        return n

    # n_minus1, n_minus2 = 1, 0
    # result = None
    
    # for f in range(n - 1):
    #     result = n_minus1 + n_minus2
    #     n_minus2 = n_minus1
    #     n_minus1 = result

    n_number, n_plus1_number = 0, 1
    for i in range(n):
        result = n_number + n_plus1_number
        n_plus1_number = n_number
        n_number = result 

    return result 

for i in range(36):
    print("{} : {}".format(i, fibonacci(i)))
