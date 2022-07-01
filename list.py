# computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
# for part in computer_parts:
#     print(part)

# number = 5
# another_number = number
# print(id(number))
# print(id(another_number))

# number = 7
# print(id(number))

# Mutable object
# List, Dic, Set, Bytearray
# computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
# another_computer_parts = computer_parts
# print(id(computer_parts))
# print(id(another_computer_parts))

# computer_parts += ["Cooler"]
# print(computer_parts)
# print(id(computer_parts))

# a = b = c = d = e = f = computer_parts
# print(a)
# # add cream
# b.append("cream")
# print(b)
# print(c)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# print(min(even))
# print(max(odd))

# append_number = even + odd
# print(append_number)
# print(len(append_number))

# print("mississippi".count("s"))

# import random

# random_number = random.randint(1, 10)
# print(random_number)


# # video 85
# current_chose = " "
# computer_parts = []
# available_part = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Mat", "HDMI Cable"]

# # valid_chice = [str(i) for i in range(1, len(available_part) + 1)]
# # print(valid_chice)

# # Same Output
# valid_chice = []
# for i in range(1, len(available_part) + 1):
#     valid_chice.append(str(i))

# while current_chose != "0":
#     if current_chose in valid_chice:
#         print("Adding {}".format(current_chose))

#         index = int(current_chose) - 1
#         chosen_part = available_part[index]
#         computer_parts.append(chosen_part)

#         # if(current_chose == "1"):
#         #     computer_parts.append("Computer")
#         # elif(current_chose == "2"):
#         #     computer_parts.append("Monitor")
#         # elif(current_chose == "3"):
#         #     computer_parts.append("Keyboard")
#         # elif(current_chose == "4"):
#         #     computer_parts.append("Mouse")
#         # elif(current_chose == "5"):
#         #     computer_parts.append("Mouse Mat")
#         # elif(current_chose == "6"):
#         #     computer_parts.append("HDMI Cable")

#     else:
#         print("Please add options from the list below: ")
#         # for parts in available_part:
#         #     print("{0}: {1}".format(available_part.index(parts) + 1, parts))
#         # Better than index to use enumerate
#         for number, parts in enumerate(available_part):
#             print("{0}: {1}".format(number + 1, parts))
    
#     current_chose = input("Enter your option: ")

# print(computer_parts)





# try by myself of 95 video
# available_part = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Mat", "HDMI Cable"]
# computer_parts = []
# current_chosen = " "

# # valid_chose = [str(i) for i in range(1, len(available_part) + 1)]

# valid_chice = []
# for i in range(1, len(available_part) + 1):
#     valid_chice.append(str(i))

# while current_chosen != "0":
#     if current_chosen in valid_chice:
#         print("Adding {}".format(current_chosen))
#         index = len(current_chose) - 1
#         chosen_parts = available_part[index]
#         computer_parts.append(chosen_parts)
        
#     else:
#         print("Please add options from the list: ")
#         for number, parts in enumerate(available_part):
#             print("{} {}".format(number + 1, parts))

#     current_chose = input("Enter your option: ")





# available_part = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Mat", "HDMI Cable"]

# valid_choices = []
# for i in range(1, len(available_part) + 1):
#     valid_choices.append(str(i))

# print(valid_choices)
# current_choice = " "
# computer_parts = []

# while current_choice != "0":
#     if current_choice in valid_choices:
#         print("Adding {}".format(current_choice))
#         index = int(current_choice) - 1
#         chosen_part = available_part[index]
#         computer_parts.append(chosen_part)

#     else:
#         print("Please add options from the list below: ")
#         for number, part in enumerate(available_part):
#             print("{0} {1}".format(number + 1, part))

#     current_choice = input("Enter your option: ")

# print(computer_parts)

### Video 97: remove the item from the list

# Documentation for build in type -python
# https://docs.python.org/3/library/stdtypes.html

# available_part = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Mat", "HDMI Cable"]

# valid_choices = []
# for i in range(1, len(available_part) + 1):
#     valid_choices.append(str(i))

# print(valid_choices)
# current_choice = " "
# computer_parts = []

# while current_choice != "0":
#     if current_choice in valid_choices:
#         index = int(current_choice) - 1
#         chosen_part = available_part[index]
#         if chosen_part in computer_parts:
#             print("Rmoving+ {}".format(current_choice))
#             computer_parts.remove(chosen_part)
#         else:
#             print("Adding {}".format(current_choice))
#             computer_parts.append(chosen_part)
#         print("Your list now contains: {}".format(computer_parts))

#     else:
#         print("Please add options from the list below: ")
#         for number, part in enumerate(available_part):
#             print("{0} {1}".format(number + 1, part))

#     current_choice = input("Enter your option: ")

# print(computer_parts)


# Video 98 shorting
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]

# even.extend(odd)
# even.sort(reverse=True)
# print(even)


### Video 100
# Documentation Build in function in python
# https://docs.python.org/3/library/functions.html
# shorted is better than sort functions



# pangram = "The quick brown fox jumped over the lazy dog"
# letters = sorted(pangram)
# print(letters)
# print(id(pangram))
# print(id(letters))


# number = [1, 5, 6, 10, 8, 9, 11, 12, 13]
# sorted_number = sorted(number)
# print(sorted_number)

### video 101 without care about case cencitive 
# pangram = "The quick brown fox jumped over the lazy dog"
# missing_letter = sorted(pangram, key=str.casefold)
# print(missing_letter)

# name = ["Graaham", "John", "terry", "eric", "Terry", "michael"]
# name.sort(key=str.casefold)
# print(name)

### Video 102


# name = ["Graaham", "John", "terry", "eric", "Terry", "michael"]
# empay_list = []
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# even.extend(odd)
# number = even + odd
# print(even)
# print(number)

# digit1 = sorted("14293597")
# digit = list("14293597")
# print(digit)
# print(digit1)

# number_general = 14293597
# number_list = list(str(number_general))
# print(number_list)
# print(list (number))

# more_number = number[:]
# more_number_copy = more_number.copy()
# print(more_number)
# print(more_number_copy)

### video 103

# computer_parts = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Mat", "HDMI Cable"]
# print(computer_parts)

# ### replace index 3 with trackball
# # computer_parts[3] = "trackball" 

# computer_parts[3:] = ["trackball"]
# print(computer_parts)


### video 104 deleting item from a list
### vide 105



# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
# del data[0:2]
# data_copy = data.copy()
# print(data)
# print(data_copy)

# min_valid = 100
# max_valid = 200

# # This code would not work as expected
# # for index, value in enumerate(data):
# #     if(value < min_valid) or (value > max_valid):
# #         del data[index]
# # print(data)

# # deleting list value then min_valid
# stop = 0
# for index, value in enumerate(data):
#     if value >= min_valid:
#         stop = index
#         break
# print(stop)
# del data[:stop]
# print(data)

# ### video 106 removing the high vlaues
# start = 0
# for index in range(len(data) -1, -1, -1):
#     if data[index] <= max_valid:
#         start = index + 1
#         break
# print(start)
# del data[start:]
# print(data)


### video 108 testing the program


### video 109 removing items from a List Backwards


# random data deleting in easy compmare than delate shorted list 
# data = [104, 101, 4, 105, 308, 5, 107, 100, 306, 106, 102, 108]
# min_valid = 100
# max_valid = 200

# for index in range(len(data) - 1, -1, -1):
#     if(data[index] < min_valid) or (data[index] > max_valid):
#         print(index)
#         del (data[index])
# print(data)

# data = [104, 101, 4, 105, 308, 5, 107, 100, 306, 106, 102, 108]
# min_valid = 100
# max_valid = 200

# top_index = len(data) - 1
# for index, value in enumerate(reversed(data)):
#     if(value < min_valid) or (value > max_valid):
#         print(top_index - index, value)
#         del data[top_index - index]
# print(data)


### video 111 Algorithms Performance 
# max_value = 100
# data_list = list(range(max_value))
# print(data_list)


### video 113 Nested List & Code style

# empty = []
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# number = [even, odd]
# print(number)

# for number_list in number:
#     print(number_list)
#     for value in number_list:
#         print(value)

### video 114 processing nested lists
### video 115 solution to nonspam challange
# menu = [
#     ["egg", "bacon"],
#     ["egg", "sausage", 'bacon'],
#     ["egg", "spam"],
#     ["egg", 'bacon', "spam"],
#     ["egg", 'bacon', 'sausage', 'spam'],
#     ["spam", 'bacon', 'sausage', 'spam'],
#     ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
#     ["spam", "egg", "spam", "spam", "bacon", "spam"],
# ]

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if(meal[index] == "spam"):
#             del meal[index]
#     print(meal)

# second way
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end= "")
#     print()


### video 116 function signature
### vide 117 print revisted

# name = "Tim"
# age = 10
# print(name, age, "Python", 2020)
# print(name, age, "Python", 2020, sep = ", ")


### video 118 The join mathod
# menu = [
#     ["egg", "bacon"],
#     ["egg", "sausage", 'bacon'],
#     ["egg", "spam"],
#     ["egg", 'bacon', "spam"],
#     ["egg", 'bacon', 'sausage', 'spam'],
#     ["spam", 'bacon', 'sausage', 'spam'],
#     ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
#     ["spam", "egg", "spam", "spam", "bacon", "spam"],
# ]

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if(meal[index] == "spam"):
#             del meal[index]
#     print(", ".join(meal))


### Video 119 The split method


# panagram = "The quick brown fox jumped over the lazy dog"
# words = panagram.split(" ")
# print("".join(words))




### start the section of Tauples
### video 121 Tuples
### A tuple is mathematical name of an ordered set of data
### Tuples are another sequence type alsong with strings, lists and range.
### Tuples differ from list
### Tuples are immutable(So cant change after they are created just like strings)


# t = "a", "b", "c", "d", "e", "f"
# print(t)

# name = "Tim"
# age = 10
# print(name, age, "Python", 2020)
# print((name, age, "Python", 2020))



### video 122 tuples are Immutable
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad company", "Bad company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
### converting tuples to list
# print(list(metallica))
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])


### video 123 unpacking a tuple
# a = b = c = d = e = f = g = h = i = j = 10, 20
# print(a)
# bappy1, bappy2 = 10, 20
# print(bappy1)

# data_list = [12, 13, 14,]
# p, q, r = data_list
# print(p)
# print(q)
# print(r)


### video 124 Practical uses for Unpacking tauples
### short version of tuple by using index and value
# for t in enumerate("abcdefg"):
#     index, value = t
#     # print(t)
#     print(index, value)


### video 125 More Unpacking
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
# name, height, width, length, price = table
# print(height * width)


### video 127 Nested Tuples and Lists
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad company", "Bad company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984)
]
# print(len(albums))
for name, artist, year in albums:
    # print(album)
    # print("Album: {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

