### video 181 What is a dictionary

# vehicles = {
#     'dream': 'Honda 250T',
#     'roadster': 'BMW R1100',
#     'er5': 'Kawasaki ER5',
#     'can-am': 'Bombardier Can-Am 250',
#     'virago': 'Yamaha XV250',
#     'tenere': 'Yamaha XT650',
#     'jimny': 'Suzuki Jimny 1.5',
#     'fiesta': 'Ford Fiesta Ghia 1.4',
# }

# my_car = vehicles["fiesta"]
# print(my_car)

# learner = vehicles.get("er5")
# print(learner)


### video 182 Adding items to a dictionaryf

# vehicles = {
#     'dream': 'Honda 250T',
#     'roadster': 'BMW R1100',
#     'er5': 'Kawasaki ER5',
#     'can-am': 'Bombardier Can-Am 250',  
#     'virago': 'Yamaha XV250',
#     'tenere': 'Yamaha XT650',
#     'jimny': 'Suzuki Jimny 1.5',
#     'fiesta': 'Ford Fiesta Ghia 1.4',
# }

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

# for key, value in vehicles.items():
#     print(key, value, sep=", ")

# vehicles["starfighter"] = "Lockheed F-104"
# vehicles["learjet"] = "Bombardier Learjet 75"
# vehicles["toy"] = "glider"
# print(vehicles)


### video 183 Change values in a dictionary

# vehicles = {
#     'dream': 'Honda 250T',
#     'roadster': 'BMW R1100',
#     'er5': 'Kawasaki ER5',
#     'can-am': 'Bombardier Can-Am 250',  
#     'virago': 'Yamaha XV250',
#     'tenere': 'Yamaha XT650',
#     'jimny': 'Suzuki Jimny 1.5',
#     'fiesta': 'Ford Fiesta Ghia 1.4',
#     "roadster": "Triumph Street Triple",
# }

# vehicles["starfighter"] = "Lockheed F-104"
# vehicles["learjet"] = "Bombardier Learjet 75"
# vehicles["toy"] = "glider"

# vehicles["virago"] = "Yamaha XV535"
# print(vehicles)


### video 184 --- Removing items from a dictionary

# vehicles = {
#     'dream': 'Honda 250T',
#     'roadster': 'BMW R1100',
#     'er5': 'Kawasaki ER5',
#     'can-am': 'Bombardier Can-Am 250',  
#     'virago': 'Yamaha XV250',
#     'tenere': 'Yamaha XT650',
#     'jimny': 'Suzuki Jimny 1.5',
#     'fiesta': 'Ford Fiesta Ghia 1.4',
#     "roadster": "Triumph Street Triple",
# }

# vehicles["starfighter"] = "Lockheed F-104"
# vehicles["learjet"] = "Bombardier Learjet 75"
# vehicles["toy"] = "glider"

# del vehicles["toy"]

# # import this 
# # print(this)

# result = vehicles.pop("f1", None)
# result1 = vehicles.pop("f2", "You wish sell the learjet and you might afford a racing car")

# plane = vehicles.pop("learjet")
# print(plane)

# bike = vehicles.pop("tenere", "not present")
# print(bike)
# print(result)                                                       


### video 186 --- Using "in" with a dictionary
### video 187 --- Dictionary menu challange solution
### video 189 --- Adding items to a dictionary

# available_parts = {
#     "1": "computer",
#     "2": "monitor",
#     "3": "keyboard",
#     "4": "mouse",
#     "5": "HDMI Cable",
#     "6": "HDMIdvd drive",
# }

# current_choice = None
# computer_parts = {}
# while current_choice != "0":
#     if current_choice in available_parts:
#         choose_part = available_parts[current_choice]
#         if current_choice in computer_parts:
#             print(f"Removing: {choose_part}")
#             available_parts.pop(current_choice)
#         else:
#             print(f"adding: {choose_part}")
#             computer_parts[current_choice] = choose_part
#         print(f"Your dictionary now contains: {computer_parts})")

#     else:
#         print("Please Select a choice from the list")
#         for key, value in available_parts.items():
#             print(f" {key}: {value}")
#         print("0: to finish")
    
#     current_choice = input("> ")



### video 190 --- Smart fridge
### video 191 --- What's for tea
### video 192 --- Using several dictionaries together
### video 193 --- Check quantities - the code
### video 194 --- Check quantities
### video 196 --- Solution: create a shopping list challange
### video 197 --- Wrong decisions don't have to be fatal
### video 198 --- The setdefault method


# pantry = {
#     "chicken": 500,
#     "lemon": 2,
#     "cumin": 24,
#     "paprika": 18,
#     "chilli powder": 7,
#     "yogurt": 300,
#     "oil": 450,
#     "onion": 5,
#     "garlic": 9,
#     "ginger": 2,
#     "tomato puree": 125,
#     "almonds": 75,
#     "rice": 500,
#     "coriander": 20,
#     "lime": 3,
#     "pepper": 8,
#     "egg": 6,
#     "pizza": 2,
#     "spam": 1,
# }

# recipes = {
#     "Butter chicken": [
#         "chicken",
#         "lemon",
#         "cumin",
#         "paprika",
#         "chilli powder",
#         "yogurt",
#         "oil",
#         "onion",
#         "garlic",
#         "ginger",
#         "tomato puree",
#         "almonds",
#         "rice",
#         "coriander",
#         "lime",
#     ],
#     "Chicken and chips": [
#         "chicken",
#         "potatoes",
#         "salt",
#         "malt vinegar",
#     ],
#     "Pizza": [
#         "pizza",
#     ],
#     "Egg sandwich": [
#         "egg",
#         "bread",
#         "butter",
#     ],
#     "Beans on toast": [
#         "beans",
#         "bread",
#     ],
#     "Spam a la tin": [
#         "spam",
#         "tin opener",
#         "spoon",
#     ],
# }

# in get method item will add
# chicken_quantity = pantry.setdefault("chicken", 0)
# print(chicken_quantity)
# bean_quantity = pantry.setdefault("bean", 0)
# print(bean_quantity)
# # in get method item wouldn't add
# ketchup_quantity = pantry.get("ketchup", 0)
# print(ketchup_quantity)

# def add_shopping_item(data: dict, item: str, amount: int) -> None:
#     """Add a tuple containing `item` and `amount` to the `data` dict."""
#     # if item in data:
#     #     data[item] += amount
#     # else:
#     #     data[item] = amount
#     data[item] = data.setdefault(item, 0) + amount


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# display_dict = {}
# for index, key in enumerate(recipes):
#     display_dict[str(index + 1)] = key

# shopping_list = {}

# while True:
#     # Display a menu of the recipes we know how to cook
#     print("Please choose your recipe")
#     print("-------------------------")
#     for key, value in display_dict.items():
#         print(f"{key} - {value}")

#     choice = input(": ")

#     if choice == "0":
#         break
#     elif choice in display_dict:
#         selected_item = display_dict[choice]
#         print(f"You have selected {selected_item}")
#         print("checking ingredients ...")
#         ingredients = recipes[selected_item]
#         print(ingredients)
#         for food_item, required_quantity in ingredients.items():
#             quantity_in_pantry = pantry.get(food_item, 0)
#             if required_quantity <= quantity_in_pantry:
#                 print(f"\t{food_item} OK")
#             else:
#                 quantity_to_buy = required_quantity - quantity_in_pantry
#                 print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
#                 add_shopping_item(shopping_list, food_item, quantity_to_buy)

# for things in shopping_list.items():
#     print(things)


### video 200 --- The `dict` documentation
### video 201 --- The remaing `dict` method

# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
# }

# pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

### make list to a dictionary key and can set default values
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

### make dictionary key to a list
# keys = d.keys()
# print(keys)

# for item in d.keys():
#     print(item)


### video 202 --- The dict `update` method

# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
# }

# pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# d2 = {
#     7: "Lucky seven",
#     10: "Ten",
#     3: "This is the new three"
# }

# d.update(d2)

# for key, value in d.items():
#     print(key, value)

# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)


### video 203 --- The dict `values` method

# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
# }

# pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# # v = d.values()
# # print(v)

# keys = list(d.keys())
# values = list(d.values())

# # will produce the same result however in first code we copy the and store in a variable
# if "four" in values:
#     index = values.index("four")
#     key = keys[index]
#     print(f"{d[key]} was found in the key {key}")

# # here we are not copying anything but iterating over the values
# for key, value in d.items():
#     if "four" in value:
#         print(f"{d[key]} was found in the key {key}")


### video 204 --- Reference to mutable objects
### Shallow_copy

# animals = {
#     "lion": "scary",
#     "elephant": "big",
#     "teddy": "cuddly",
# }

# things = animals
# things = animals.copy()
# animals["teddy"] = "toy"
# print(things["teddy"])


### video 205 --- Shallow copy
### video 206 --- Shallow copy step-by-step
### documentation for shallow copy --- https://docs.python.org/3/library/copy.html

# lion_list = ["scary", "big", "cat"]
# elephant_list = ["big", "gray", "wrinkled"]
# teddy_list = ["cuddly", "stuffed"]

# animals = {
#     "lion": lion_list,
#     "elephant": elephant_list,
#     "teddy": teddy_list,
# }

# things = animals.copy()

# things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"])


### video 207 --- Deep copy

# import copy

# lion_list = ["scary", "big", "cat"]
# elephant_list = ["big", "gray", "wrinkled"]
# teddy_list = ["cuddly", "stuffed"]

# animals = {
#     "lion": lion_list,
#     "elephant": elephant_list,
#     "teddy": teddy_list,
# }

# things = copy.deepcopy(animals)

# things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"])


### video 208 --- Simple deep copy solution

### video 209 --- Hash function

### video 210 --- A really bad hashing function

# data = [
#     ("orange", "a sweet, orange, citrus fruit"),
#     ("apple", "good for making cider"),
#     ("lemon", "a sour, yellow citrus fruit"),
#     ("grape", "a small, sweet fruit growing in bunches"),
#     ("melon", "sweet and juicy"),
# ]

# print(ord("a"))
# # print(ord("b"))
# # print(ord("z"))


# def simple_hash(s: str) -> int:
#     """A ridiculously simple hashing function"""
#     basic_hash = ord(s[0])
#     return basic_hash % 10


# for key, value in data:
#     h = simple_hash(key)
#     # h = hash(key)
#     print(key, h)


### video 211 --- Hash tables

# data = [
#     ("orange", "a sweet, orange, citrus fruit",),
#     ("apple", "good for making cider"),
#     ("lemon", "a sour, yellow citrus fruit"),
#     ("grape", "a small, sweet fruit growing in bunches"),
#     ("melon", "sweet and juicy"),
# ]

# def simple_hash(s: str) -> int:
#     """A ridiculously simple hashing function"""
#     basic_hash = ord(s[0])
#     return basic_hash % 10

# keys = ["a"] * 10
# values = keys.copy()
# for key, value in data:
#     h = simple_hash(key)
#     print(key, h)

#     keys[h] = key
#     values[h] = value

# print(keys, " : ", values)


### video 216 --- Introduce set

### video 217 --- Python set

# farm_animal = {"cow", "sheep", "hen", "goat", "horse"}
# print(farm_animal)

# for animal in farm_animal:
#     print(animal)

### video 218 --- Implications of sets being unordered
### set is unordered 
### set can't be slice 
### set can't be dupliccate
### set is similar to list or tuple but more resticted 


# farm_animal = {"cow", "sheep", "hen", "goat", "horse"}
# goat = farm_animal[3]
# print(farm_animal)

# more_animal = {"cow", "sheep", "hen", "horse", "goat"}
# if farm_animal == more_animal:
#     print("Both set are equal")
# else:
#     print("Set are not equal")


### video 219 --- Set membership
### video 220 --- Testing set membership is fast

# choice = "-"  # initialise choice to something invalid
# while choice != "0":
#     if choice in set("12345"):
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")

#     choice = input("-> ")


### video 221 --- Adding items to a set

# numbers = {*""}
# numbers = {*{}}

# numbers = set()
# print(type(numbers))
# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = input("Please enter your next value: ")
#     numbers.add(next_value)

# print(numbers)


### video 222 --- Using a set to remove duplicate values

# data = ["blue", "green", "yellow", "orange", "black", "red", "yellow", "orange", "black"]
# we will get a sorted list with no duplicates
# unique_data = sorted(set(data))
# print(unique_data)

# create a list of unique colours, keeping the order they appeared

# unique_data2 = list(dict.fromkeys(data))
# print(unique_data2)


### video 223 --- Deleting items from set
# there are 3 ways to delete a item form set

# small_ints = set(range(21))
# print(small_ints)

# delete all the items from the set
# small_ints.clear()
# print(small_ints)
# Remove a item form the set
# small_ints.discard(10)
# small_ints.remove(11)

# print(small_ints)

### video 224 --- The `discard` method

# travel_mode = {"1": "car", "2": "plane"}

# items = {
#     "can opener",
#     "fuel",
#     "jumper",
#     "knife",
#     "matches",
#     "razor blades",
#     "razor",
#     "scissors",
#     "shampoo",
#     "shaving cream",
#     "shirts (3)",
#     "shorts",
#     "sleeping bag(s)",
#     "soap",
#     "socks (3 pairs)",
#     "stove",
#     "tent",
#     "mug",
#     "toothbrush",
#     "toothpaste",
#     "towel",
#     "underwear (3 pairs)",
#     "water carrier",
# }

# restricted_items = {
#     "catapult",
#     "fuel",
#     "gun",
#     "knife",
#     "razor blades",
#     "scissors",
#     "shampoo",
# }

# print("Please choose your mode of travel:")
# for key, value in travel_mode.items():
#     print(f"{key}: {value}")
#     # Python 3.5 and earlier
#     # print("{}: {}".format(key, value))

# mode = "-"
# while mode not in travel_mode:
#     mode = input("> ")

# if mode == "2":
#     # travelling by plane, remove restricted items
#     for restricted_item in restricted_items:
#         # if instand of discard, use remove then it will through error because one item in restricted_items have but not in items
#         items.discard(restricted_item)

# # print the packing list
# print("You need to pack:")
# for item in sorted(items):
#     print(item)


### video `remove` method

# drugs
# amlodipine = ("amlodipine", "Blood pressure")
# buspirone = ("buspirone", "Anxiety disorders")
# carbimazole = ("carbimazole", "Antithyroid agent")
# citalopram = ("citalopram", "Antidepressant")
# edoxaban = ("edoxaban", "anti-coagulant")
# erythromycin = ("erythromycin", "Antibiotic")
# lusinopril = ("lusinopril", "High blood pressure")
# metformin = ("metformin", "Type 2 diabetes")
# methotrexate = ("methotrexate", "Rheumatoid arthritis")
# paracetamol = ("paracetamol", "Painkiller")
# propranol = ("propranol", "Beta blocker")
# simvastatin = ("simvastatin", "High cholesterol")
# warfarin = ("warfarin", "anti-coagulant")

# # Drugs that shouldn't be taken together
# adverse_interactions = [
#     {metformin, amlodipine},
#     {simvastatin, erythromycin},
#     {citalopram, buspirone},
#     {warfarin, citalopram},
#     {warfarin, edoxaban},
#     {warfarin, erythromycin},
#     {warfarin, amlodipine},
# ]

# # Patient prescriptions
# patients = {
#     "Anne": {methotrexate, paracetamol},
#     "Bob": {carbimazole, erythromycin, methotrexate, paracetamol},
#     "Charley": {buspirone, lusinopril, metformin},
#     "Denise": {amlodipine, lusinopril, metformin, warfarin},
#     "Eddie": {amlodipine, propranol, simvastatin, warfarin},
#     "Frank": {buspirone, citalopram, propranol, warfarin},
#     "Georgia": {carbimazole, edoxaban, warfarin},
#     "Helmut": {erythromycin, paracetamol, propranol, simvastatin},
#     "Izabella": {amlodipine, citalopram, simvastatin, warfarin},
#     "John": {simvastatin},
#     "Kenny": {amlodipine, citalopram, metformin},
# }

# trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]

# # Remove warfarin and add Edoxaban
# for patient in trial_patients:
#     prescription = patients[patient]
    
#     if warfarin in prescription:
#         prescription.remove(warfarin)
#         prescription.add(edoxaban)
#     else: 
#         print(f"Patient {patient} is not taking warfarin.")
#         print(f"Please remove {patient} from the trial")
        
#     print(patient, prescription)


### video 226 --- The `pop` method

# trail_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

# drugs
# amlodipine = ("amlodipine", "Blood pressure")
# buspirone = ("buspirone", "Anxiety disorders")
# carbimazole = ("carbimazole", "Antithyroid agent")
# citalopram = ("citalopram", "Antidepressant")
# edoxaban = ("edoxaban", "anti-coagulant")
# erythromycin = ("erythromycin", "Antibiotic")
# lusinopril = ("lusinopril", "High blood pressure")
# metformin = ("metformin", "Type 2 diabetes")
# methotrexate = ("methotrexate", "Rheumatoid arthritis")
# paracetamol = ("paracetamol", "Painkiller")
# propranol = ("propranol", "Beta blocker")
# simvastatin = ("simvastatin", "High cholesterol")
# warfarin = ("warfarin", "anti-coagulant")

# patients = {
#     "Anne": {methotrexate, paracetamol},
#     "Bob": {carbimazole, erythromycin, methotrexate, paracetamol},
#     "Charley": {buspirone, lusinopril, metformin},
#     "Denise": {amlodipine, lusinopril, metformin, warfarin},
#     "Eddie": {amlodipine, propranol, simvastatin, warfarin},
#     "Frank": {buspirone, citalopram, propranol, warfarin},
#     "Georgia": {carbimazole, edoxaban, warfarin},
#     "Helmut": {erythromycin, paracetamol, propranol, simvastatin},
#     "Izabella": {amlodipine, citalopram, simvastatin, warfarin},
#     "John": {simvastatin},
#     "Kenny": {amlodipine, citalopram, metformin},
# }

# while trail_patients: 
#     patient = trail_patients.pop()
#     print(patient, end=": ")
#     prescreption = patients[patient]
#     print(prescreption)


### video 227 --- Set Union in practice
### video 228 --- Union Update

# amlodipine = ("amlodipine", "Blood pressure")
# buspirone = ("buspirone", "Anxiety disorders")
# carbimazole = ("carbimazole", "Antithyroid agent")
# citalopram = ("citalopram", "Antidepressant")
# edoxaban = ("edoxaban", "anti-coagulant")
# erythromycin = ("erythromycin", "Antibiotic")
# lusinopril = ("lusinopril", "High blood pressure")
# metformin = ("metformin", "Type 2 diabetes")
# methotrexate = ("methotrexate", "Rheumatoid arthritis")
# paracetamol = ("paracetamol", "Painkiller")
# propranol = ("propranol", "Beta blocker")
# simvastatin = ("simvastatin", "High cholesterol")
# warfarin = ("warfarin", "anti-coagulant")

# adverse_interactions = [
#     {metformin, amlodipine},
#     {simvastatin, erythromycin},
#     {citalopram, buspirone},
#     {warfarin, citalopram},
#     {warfarin, edoxaban},
#     {warfarin, erythromycin},
#     {warfarin, amlodipine},
# ]

# meds_to_watch = set()

# for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interaction)
    ### will produce the same result
    # meds_to_watch = meds_to_watch | interaction

    ### update method
    # meds_to_watch.update(interaction)
    ### another way to update
    # meds_to_watch =| interaction

# print(sorted(meds_to_watch))

### video 230 --- Advantage of the set operation method over the operators

# amlodipine = ("amlodipine", "Blood pressure")
# buspirone = ("buspirone", "Anxiety disorders")
# carbimazole = ("carbimazole", "Antithyroid agent")
# citalopram = ("citalopram", "Antidepressant")
# edoxaban = ("edoxaban", "anti-coagulant")
# erythromycin = ("erythromycin", "Antibiotic")
# lusinopril = ("lusinopril", "High blood pressure")
# metformin = ("metformin", "Type 2 diabetes")
# methotrexate = ("methotrexate", "Rheumatoid arthritis")
# paracetamol = ("paracetamol", "Painkiller")
# propranol = ("propranol", "Beta blocker")
# simvastatin = ("simvastatin", "High cholesterol")
# warfarin = ("warfarin", "anti-coagulant")

# adverse_interactions = [
#     {metformin, amlodipine},
#     {simvastatin, erythromycin},
#     {citalopram, buspirone},
#     {warfarin, citalopram},
#     {warfarin, edoxaban},
#     {warfarin, erythromycin},
#     {warfarin, amlodipine},
# ]

# meds_to_watch = set()

# meds_to_watch.update(*adverse_interactions)

# print(sorted(meds_to_watch))


### video 231 --- Set intersection

# from typing import Generator

# def squares_generator(n: int) -> Generator[int, None, None]:
#     """Generator to return the perfect squares less than `n`."""
#     if n > 0:
#         i = next_square = 1
#         while next_square < n:
#             yield next_square
#             i += 1
#             next_square = i * i


# def primes_generator(n: int) -> Generator[int, None, None]:
#     """
#     Very naive implementation of the Sieve of Eratosthenes to generate prime numbers.

#     This is *not* suitable for production use.
#     For an optimised algorithm, check out the work by Tim Peters et al @ActiveState, and Will Ness.
#     https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/19391111#19391111

#     :param n: The number to generate primes up to.
#     :return: A generator of all positive prime numbers less than or equal to `n`.
#     """
#     if n >= 2:
#         # start with the set of positive odd integers from 3 to `n`, inclusive.
#         integers = set(range(3, n + 1, 2))
#         # There's no point removing multiples of 2 from odd numbers.
#         yield 2
#         next_prime = 3
#         while integers:
#             yield next_prime
#             # Remove all multiples of `next_prime`.
#             integers.difference_update(range(next_prime, n + 1, 2 * next_prime))
#             next_prime = min(integers, default=None)  # None if set is empty.


# if __name__ == '__main__':
#     print("Squares less than 1000:")
#     squares = list(squares_generator(1000))
#     print(squares)
#     print("Generated {} squares.".format(len(squares)))

#     print("Primes up to 1000")
#     primes = set(primes_generator(1000))
#     print(sorted(primes))
#     print("Generated {} primes.".format(len(primes)))

#     check = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
#              31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
#              73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
#              127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
#              179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
#              233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
#              283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
#              353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
#              419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
#              467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
#              547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
#              607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
#              661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
#              739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
#              811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
#              877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
#              947, 953, 967, 971, 977, 983, 991, 997}
#     print(primes == check)

# evens = set(range(0, 50, 2))
# odds = set(range(1, 50, 2))

# print(evens)
# print(odds)

# primes = set(primes_generator(100))
# print(primes)

# squares = set(squares_generator(100))
# print(squares)

# print(odds.intersection(squares))
# print(evens & squares)

# ## pass an iterable to the method
# even_squares = evens.intersection(squares_generator(100))
# print(even_squares)


### video 232 --- Set intersection in practice

# trial_1 = {"Bob", "Charley", "Georgia", "John"}
# trial_2 = {"Anna", "Charley", "Eddie", "Georgia"}

# Check_set = trial_1.intersection(trial_2)
# print(Check_set)

# farm_animal = {"Sheep", "hen", "cow", "horse", "goat"}
# wild_animal = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
# potential_rides = { "donkey", "horse", "camel"}

# intersection = farm_animal & wild_animal & potential_rides
# mounts = farm_animal.intersection(wild_animal, potential_rides)
# print(intersection)
# print(mounts)


### video 233 --- Set difference
### video 234 --- Set difference in Practice

# from typing import Generator

# def squares_generator(n: int) -> Generator[int, None, None]:
#     """Generator to return the perfect squares less than `n`."""
#     if n > 0:
#         i = next_square = 1
#         while next_square < n:
#             yield next_square
#             i += 1
#             next_square = i * i


# def primes_generator(n: int) -> Generator[int, None, None]:
#     """
#     Very naive implementation of the Sieve of Eratosthenes to generate prime numbers.

#     This is *not* suitable for production use.
#     For an optimised algorithm, check out the work by Tim Peters et al @ActiveState, and Will Ness.
#     https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/19391111#19391111

#     :param n: The number to generate primes up to.
#     :return: A generator of all positive prime numbers less than or equal to `n`.
#     """
#     if n >= 2:
#         # start with the set of positive odd integers from 3 to `n`, inclusive.
#         integers = set(range(3, n + 1, 2))
#         # There's no point removing multiples of 2 from odd numbers.
#         yield 2
#         next_prime = 3
#         while integers:
#             yield next_prime
#             # Remove all multiples of `next_prime`.
#             integers.difference_update(range(next_prime, n + 1, 2 * next_prime))
#             next_prime = min(integers, default=None)  # None if set is empty.


# if __name__ == '__main__':
#     print("Squares less than 1000:")
#     squares = list(squares_generator(1000))
#     print(squares)
#     print("Generated {} squares.".format(len(squares)))

#     print("Primes up to 1000")
#     primes = set(primes_generator(1000))
#     print(sorted(primes))
#     print("Generated {} primes.".format(len(primes)))

#     check = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
#              31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
#              73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
#              127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
#              179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
#              233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
#              283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
#              353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
#              419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
#              467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
#              547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
#              607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
#              661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
#              739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
#              811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
#              877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
#              947, 953, 967, 971, 977, 983, 991, 997}
#     print(primes == check)

# evens = set(range(0, 50, 2))
# odds = set(range(1, 50, 2))

# print(evens)
# print(odds)

# primes = set(primes_generator(100))
# print(primes)

# squares = set(squares_generator(100))
# print(squares)

# print(odds.difference(primes))
# print(odds - primes)


### video 235 --- Set symmetric difference

# morning = {"java", "c", "ruby", "lisp", "c#"}
# afternoon = {"Python", "c#", "java", "c", "ruby"}

# possible_course = morning ^ afternoon
# possible_course = set(morning).symmetric_difference(afternoon)
# print(possible_course)


### video 236 --- Subset and supersets
### video 237 --- Subset and supersets in Python

# animals = {"Turtle", "Horse", "Robin", "Python", "Swallow", "Hedgehog", "Wren", "Aardvark", "Cat"}
# birds = {"Robin", "Swallow", "Wren"}
# print(f"Birds is a subset of animals {birds.issubset(animals)}")
# print(f"Animals is a superset of birds {animals.issuperset(birds)}")

# ### subset and supper set
# print(birds <= animals)
# print(animals >= birds)
# print()
# ### proper set
# print(birds == animals)
# print(birds < animals)
# print(animals > birds)


### video 238 --- Practical application of subsets and supersets

required_skills = ["python", "github", "linux"]

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):
        interviewees.add(candidate)

print(interviewees)