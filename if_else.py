

# answer = 5

# guess = int(input("Please guess number between 1 to 10: "))
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# from random import Random
# random_number = random()
# print(random_number)

# if(guess == answer):
#     print("You got in first attempt")
# else:
#     if(guess > answer):
#         print("please guess less number than that")
#     else:
#         print("please guess large number than that")
#     guess = input("Try second time for your attempt: ")
#     if(guess == answer):
#         print("This time you got it right")
#     else:
#         print("opps! need more time guess it")


# age = int(input("How old are you? "))

# if(age >= 16  and age <= 65):
#     print("Have a good day in work")
# else:
#     print("your age not capable for job")

# day = "Monday"
# temperature = 30
# raining = True
# if day == "Saturday" and temperature > 27 and not raining:
#     print("Go for swimming")
# else:
#     print("Learn python")

# if 0:
#     print("True")
# else:
#     print("False")

# name = input("Enter your name: ")
# # if name:
# if name != "":
#     print(f"Hello, {name}")
# else:
#     print("Are you a person without a name? ")

# country_name = "Bangladesh"
# if("Ban" in country_name.casefold()):
#     print("Your compare country is in the string")

name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print(f"I am {name} and {age} years old. So, can join in the vacation")
else:
    print("So, Sir/Madam you may try different enjoyment tools")