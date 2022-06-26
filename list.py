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
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
even.sort(reverse=True)
print(even)

