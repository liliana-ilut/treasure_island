print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

#there are 3 choices in this situation
first_choice = input("You\'ve came to a crossroad. Would you like to go Left or Right? ")

#lower the characters for the answers
fcl = first_choice.lower()

if fcl == "right":
    print("Finito la comedia! This was a short game for you!")
elif fcl == "left":
    second_choice = input("There is a river you need to cross. Would you like to swim across the Black River or wait for a boat? ")
    scl = second_choice.lower()
    if scl == "swim":
        print ("Game over! You were attacked by a water monster!")
    elif scl == "wait":
        third_choice = input("You\'ve arrived to a house with 3 doors: Red, Blue or Yellow. Which door would you like to open? ")
        tcl = third_choice.lower()
    # print(third_choice)
        if tcl == "blue":
            print("Game over! You were eaten by warewolves")
        elif tcl == "yellow":
            print("Congratulation!!! You found the treasure! You can go celebrate !!")
        elif tcl == "red" :
            print("You were burnt by fire! Game over!")
        else:
            print("Game over")    
    else:
        print ("Game over! You were attacked by a water monster!") 
else:
    print("Finito la comedia! This was a short game for you!")  




