import random

def project_greeting():
    message = "Armando's Day Trip Generator"
    print(message)

def options_list():
    destinations = ["Gondor", "The Death Star", "Jurassic Park", "Willy Wonka's Chocolate Factory", 
        "Hogwarts School of Witchcraft & Wizadry", "Stanly Hotel", "King's Landing", "Gotham City"]
    restaraunts = ["Bob's Burgers", "The Three BroomSticks", "The Mos Eisley Cantina", "The Krusty Crab",
     "Pizza Planet", "La Ratatouille", "Los Pollos Hermanos", "Gus's Galaxy Grill"]
    entertainment = ["Learning Magic", "Running for your life", "Battling Jedi's", "Ruling a Kingdom",
    "Becoming a hero", "Hunting big lizards", "Carnival Ride", "Live Crowning event of new King"]
    mode_of_transport = ["Flying on Giant Eagles", "Millenium Falcon flight", "Jeep", "River Boat",
    "Broomstick", "Teleportation", "Horseback drawn carriage", "Batmobile"]

    place = "Destination: " + random.choice(destinations)
    food = "Restaraunt: " + random.choice(restaraunts)
    activity = "Entertainment: " + random.choice(entertainment)
    transport = "Transportation: " + random.choice(mode_of_transport)

    return [place, food, activity, transport]

def display_options(options):
    print()
    for option in options:
        print(option)
    
def satisfaction(trip):
    print()
    while True:
        prompt = input("Are the details of the trip acceptable? Y or N: ")
        if prompt != "Y":
            final_trip = "Here are your trip details! "
            print()
            print(final_trip)
            trip = options_list()
            display_options(trip)
            print()
        else:  
            final_trip = "Here are your final trip details! "
            print()
            print(final_trip)
            display_options(trip)
            print()
            break

def main():
    project_greeting()
    options = options_list()
    display_options(options)
    satisfaction(options)

main()