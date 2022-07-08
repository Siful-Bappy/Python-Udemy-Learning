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

from numpy import choose


pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

display_dict = {}

for index, key in enumerate(recipes):
    # print("{}: {}".format(index + 1, key))
    display_dict[str(index + 1)] = key

while True:
    print("Please choose your recipe")
    print("-" * 25)
    for key, value in display_dict.items():
        print("{}: {}".format(key, value))
    
    choose = input("-> ")
    if choose == "0":
        break
