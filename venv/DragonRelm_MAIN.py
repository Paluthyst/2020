import random
import time

def displayIntro():
    print("You wake up in a strange land whith no memory. Around you dragons fly free. In front of you, ")
    print("You see two caves in front of you. In one cave lies the friendly dragon. ")
    print("He shares his treasue with all who pass through. In the other cave lies a terrible dragon,  ")
    print("one who is greedy and hungry. He will eat you without a second thought. ")
def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you choose traveler? ) (1 or 2 ) ")
        cave = input()
    return cave
def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(3.5)
    print("The water dripping from the celing and the breeze coming from the back of the cave make you uneasy...")
    time.sleep(5)
    print("Without warning a large dragon launches itself in your path. His jaw opens suddenly, revealing it's massive teeth. You close your eyes in fear and...")
    time.sleep(7)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("After what feels like an eternity you open your eyes only to see sparkling jewels and rings for you to take.")
    else:
        print("You feel no pain as the dragon promptly eats you whole.")
playAgain ="yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Would you like to re-awaken? (yes or no)")
    playAgain = input()
