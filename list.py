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

# video 85
current_chose = " "
computer_parts = []
available_part = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Mat", "HDMI Cable"]

while current_chose != "0":
    if current_chose in "123456":
        print("Adding {}".format(current_chose))
        if(current_chose == "1"):
            computer_parts.append("Computer")
        elif(current_chose == "2"):
            computer_parts.append("Monitor")
        elif(current_chose == "3"):
            computer_parts.append("Keyboard")
        elif(current_chose == "4"):
            computer_parts.append("Mouse")
        elif(current_chose == "5"):
            computer_parts.append("Mouse Mat")
        elif(current_chose == "6"):
            computer_parts.append("HDMI Cable")

    else:
        print("Please add options from the list below: ")
        # for parts in available_part:
        #     print("{0}: {1}".format(available_part.index(parts) + 1, parts))
        # Better than index to use enumerate
        for number, parts in enumerate(available_part):
            print("{0}: {1}".format(number + 1, parts))
    
    current_chose = input("Enter your option: ")

print(computer_parts)