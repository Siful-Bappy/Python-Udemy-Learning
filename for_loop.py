# parrot = "Norwegian BLUE"

# for i in parrot:
#     print(i)

# number = "9,223;372:036 854,775;807"
# separators = number[1::4]
# print(separators)
# separators = ""
# for char in number:
#     if not char.isnumeric():
#         separators = separators + char
# print(separators)


# for i in range(1, 21):
#     print("i is now {}".format(i))

# backward range
# for i in range(10, 0, -2):
#     print("i is now {}".format(i))

# age = int(input("How old are you?"))
# if age in range(16, 66):
#     print("Have a good day at work")
# else:
#     print("Enjoy you day")

# for i in range(1, 21):
#     for j in range(1, 12):
#         if(j == 11):
#             continue
#         print("{} times {} is {}".format(j, i, j*i))
#     print("-" * 30)

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     print(item)


# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# item_to_find = "spam"
# found_at = None

# for index in range(len(shopping_list)):
#     if(shopping_list[index] == item_to_find):
#         found_at = index
#         break

# if found_at is not None:
#     print("Item found at position {}".format(found_at))
# else:
#     print("{} not found".format(item_to_find))

# while loop
# i = 1
# while i < 11:
#     print("i is now {}".format(i))
#     i += 1


# available_exits = ["north", "south", "east", "west"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game over")
#         break
# print("aren't you glad you got out of there")


# import random
# answer = random.randint(1, 10)
# print("Answer: ", answer)

# guess = int(input("Please guess a number between 1 to 10: "))
# if guess == answer:
#     print("You got in the first attempt")
# else:
#     if(guess < answer):
#         print("Please guess higher number")
#     else:
#         print("Plese guess lower number")
#     guess = int(input("Please guess a number between 1 to 10: "))
#     if guess == answer:
#         print("Well done, this time you guess it right")
#     else:
#         print("Better luck next time")


# import random
# answer = random.randint(1, 10)
# print("Answer: ", answer)
# guess = int(input("Please guess a number between 1 to 10: "))

# while answer != guess:
#     guess = int(input("Please guess again a number between 1 to 10: "))
#     if answer == guess:
#         print("You got it right")
#     else:
#         print("Try again")
# +
# low = 1
# high = 1000
# print("Please think of a number between {} and {}".format(low, high))
# input("Pass ENTER to start")
# guesses = 1
# while True:
#     guess = low + (high - low) // 2
#     high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct ".format(guess)).casefold()
#     if high_low == "h":
#         low = guess + 1
#     elif high_low == "l":
#         high = guess - 1
#     elif high_low == "c":
#         print("I got it in {} guesses!".format(guesses))
#         break
#     else:
#         print("Please enter h, l or c")
#     guesses = guesses + 1

# else condition in loop
numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        print(f"{number} number is unceptable")
        break
else:
    print("All the numbers is fine")