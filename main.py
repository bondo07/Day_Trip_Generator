import random
def projectgreeting():
    print("Armando's Day Trip Generator")

projectgreeting()

# def place():
#     destinations = ["Gondor", "The Death Star", "Jurassic Park", "Willy Wonka's Chocolate Factory", 
#         "Hogwarts School of Witchcraft & Wizadry", "Stanly Hotel", "King's Landing", "Gotham City"]
#     chosen_d = random.choice(destinations)
#     destination = ""
#     if destination in chosen_d:
#             print(chosen_d)
# # place()

# def food():
#     restaurants = ["Bob's Burgers", "The Three BroomSticks", "The Mos Eisley Cantina", "The Krusty Crab",
#      "Pizza Planet", "La Ratatouille", "Los Pollos Hermanos", "Gus's Galaxy Grill"]
#     chosen_r = random.choice(restaurants)
#     restaraunt = ""
#     if restaraunt in chosen_r:
#         print(chosen_r)

# # food()

# def entertainment():
#     entertainment_opt = ["Learning Magic", "Running for your life", "Battling Jedi's", "Ruling a Kingdom",
#     "Becoming a hero", "Hunting big lizards", "Carnival Ride", "Live Crowning event of new King"]
#     chosen_e = random.choice(entertainment_opt)
#     entertainments = ""
#     if entertainments in chosen_e:
#         print(chosen_e)
# # enterainment()

# def transport():
#     mode_of_transport = ["Flying on giant Eagles", "Millenium Falcon flight", "Jeep", "River Boat",
#     "Broomstick", "Teleportation", "Horseback drawn carriage", "Batmobile"]
#     chosen_t = random.choice(mode_of_transport)
#     transportation = ""
#     if transportation in chosen_t:
#         print(chosen_t)

# transport()

# trip_features = place(), food(), entertainment(), transport()

# trip_features

def options_list():
    destinations = ["Gondor", "The Death Star", "Jurassic Park", "Willy Wonka's Chocolate Factory", 
        "Hogwarts School of Witchcraft & Wizadry", "Stanly Hotel", "King's Landing", "Gotham City"]
    chosen_d = random.choice(destinations)
    destination = ""
    if destination in chosen_d:
            print(chosen_d)
    restaurants = ["Bob's Burgers", "The Three BroomSticks", "The Mos Eisley Cantina", "The Krusty Crab",
     "Pizza Planet", "La Ratatouille", "Los Pollos Hermanos", "Gus's Galaxy Grill"]
    chosen_r = random.choice(restaurants)
    restaraunt = ""
    if restaraunt in chosen_r:
        print(chosen_r)
    entertainment_opt = ["Learning Magic", "Running for your life", "Battling Jedi's", "Ruling a Kingdom",
    "Becoming a hero", "Hunting big lizards", "Carnival Ride", "Live Crowning event of new King"]
    chosen_e = random.choice(entertainment_opt)
    entertainments = ""
    if entertainments in chosen_e:
        print(chosen_e)
    mode_of_transport = ["Flying on giant Eagles", "Millenium Falcon flight", "Jeep", "River Boat",
    "Broomstick", "Teleportation", "Horseback drawn carriage", "Batmobile"]
    chosen_t = random.choice(mode_of_transport)
    transportation = ""
    if transportation in chosen_t:
        print(chosen_t)
options_list() 