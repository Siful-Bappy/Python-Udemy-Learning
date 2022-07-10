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

choice = "-"  # initialise choice to something invalid
while choice != "0":
    if choice in set("12345"):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input("-> ")



