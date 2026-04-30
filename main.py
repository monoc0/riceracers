import time, modules

recipes = []
didMinigame = False
score = 0

title = r"""
                                                                                                                         
,------. ,--.                           ,------. ,--.          ,--.             ,------. ,--.                            
|  .--. '`--',--,--,  ,---.,--. ,--.    |  .--. '|  | ,--,--.,-'  '-. ,---.     |  .--. '`--' ,---.  ,---. ,---.  ,---.  
|  '--' |,--.|      \| .-. |\  '  /     |  '--' ||  |' ,-.  |'-.  .-'| .-. :    |  '--' |,--.| .-. :| .--'| .-. :(  .-'  
|  | --' |  ||  ||  |' '-' ' \   '      |  | --' |  |\ '-'  |  |  |  \   --.    |  | --' |  |\   --.\ `--.\   --..-'  `) 
`--'     `--'`--''--' `---'.-'  /       `--'     `--' `--`--'  `--'   `----'    `--'     `--' `----' `---' `----'`----'  
                           `---'                                                                                         
a demo for CS2
"""

menu = modules.menu.copy()

print(title)
time.sleep(2)
user = input("Enter your username: ").strip()
print(f"Hello and good day po, {user}, to our program! Here you will explore the vast Filipino cuisine, and discover famous recipes and facts of Philippine cuisines!")
time.sleep(2)
print("Here is a menu of the main and side dishes, drinks and desserts")
modules.menuGet()

while True:
    try:
        choiceAmount = int(input("Input how many dishes, drinks, or desserts you want to learn more! (input is limited from 1 to 12, special interaction with 12): "))
        if not (1 <= choiceAmount <= 12):
            raise ValueError
        break
    except ValueError:
        print("INVALID INPUT TYPE. Input an integer between 1 to 12.")

modules.clear()
modules.menuGet()
if not choiceAmount == 12:

    for i in range(choiceAmount):
        isFound = False
        while not isFound:
            addRecipe = input("Inquire a recipe. Must be from the menu.").strip().lower()
            for cat in menu:
                for item in cat:
                    if isFound == False and addRecipe == item.lower():
                        recipes.append(item)
                        isFound = True
                        break
                if isFound: break
            if not isFound:
                print("Item not found in the menu, please retry.")
                time.sleep(1)
        modules.clear()
        print(f"Current Menu: {recipes}")
        modules.menuGet()

else:
    for cat in menu:
        for item in cat:
            recipes.append(item)

    print(f"Current Menu: {recipes}")
    modules.menuGet()