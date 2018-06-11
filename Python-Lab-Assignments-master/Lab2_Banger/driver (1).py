from Banger import *
from random import randint
import time

#Registration from the file competitors.txt
cars = []

car_file = open("competitors.txt")

for each in car_file:
    car, type_car = each.split('\t')
    new_entry = Banger(car.strip(), type_car.strip())
    cars.append(new_entry)
    
print("There are now", len(cars), "cars in this here demolition derby.")    
print("Registration is now closed.  Here's who we have in our race:\n")
for each in cars:
    print(each)

#Welcome
print("\nAnd now it's time for the race!\n")
print("Welcome ladies and gentlemen to the CSE 1384 Demolition Derby.")
print("We have cars in the arena to rock your world with all of the smashing")
print("and crashing that you could ever hope for.  It promises to be an")
print("exciting night.\n")

print("Our returning champion, " + cars[0].get_driver()+ ", has come tonight")
print("with his newest" + cars[0].get_model()+ ".")
print("The race hasn't started yet so he has " + str(cars[0].get_hits()) + "hits so far,")
print("but is he ever mobile.\nYee-haa!  Look at him move.  Yessiree, it should")
print("be a fine show.")


#Start of commented out section -- starting the derby

print("Let's start this game.\n\nBANG!\n\n")

while len(cars) > 1:    #Continue until one champ remains
    if len(cars) < 5:
        print("We're down to", len(cars), "cars in the race.")
    else:
        print("We still have", len(cars), "cars in the race.")

    car_total = len(cars)
    #Collisions
    basher = randint(0, car_total - 1)
    bashed = randint(0, car_total - 1)
    #A car can't hit itself
    while basher == bashed:
        bashed = randint(0, car_total - 1)
    
    print(cars[basher].get_driver(), "just hit", cars[bashed].get_driver(), "and...")

    hit_hard = randint(1, 10)
    if hit_hard > 6: #Can no longer move
        out = cars.pop(bashed)
        print("Yes!  It looks like he can't get his ol' ", out.get_model(), "movin'.")
        print("He's out of the game!")
        
    else: #Add a hit to the car
        cars[bashed].add_hit()
        print("But he's still moving -- so he's still in the game.")
    print("\n")
    time.sleep(2)

#Ending announcements
print("The crowd is going WILD!  There's only one car left now.")
print("So with ", cars[0].get_hits(), "hits in this game, our new champion is.....")
print("drum-roll please.....\n")
print(cars[0].get_driver() + "!!!")
print("\nEverybody be sure to say a big CONGRATULATIONS to our champion.")
print("And be sure to come back next year, but until then, keep on crashin'")
print("and a-smashin'!")
print()
        

