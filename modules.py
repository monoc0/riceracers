import os, subprocess, random

main = ['Adobo', 'Sinigang', 'Lechon']
side = ['Lomi', 'Sopas', 'Munggo']
dessert = ['Halo-Halo', 'Taho', 'Leche Flan']
drinks = ['Gulaman', 'Buko Juice', 'Magic Water']
menu = [main,side,dessert,drinks]

main_desc = {'Adobo':"Adobo, a national delicacy unique for it's savory taste and pride of the Filipinos. Adobo is flavorful with its combination soy sauce, vinegar, sugar, peppercorns, bay leaves and lots more! '', 'Sinigang': 'A sour soup usually using shrimp or pork added with tamarind, vegtables, and gabi to enhance its flavor!', 'Lechon': 'A whole roasted pig typically served in parties or gatherings, known for it crispy skin, fatty and delicious meat!
\n Lechon is stuffed with a multitude of herbs and spices inside the body of the pig, when cutting it open you will be hit with an array of flavorous smells!'}
side_desc = {'Lomi': '', 'Sopas': 'Sopas is a creamy macaroni soup paired with hotdog and vegtables, and typically added with evaporated milk!', 'Munggo': 'a'}
dessert_desc = {'Halo-Halo': 'a', 'Taho': 'a', 'Leche Flan': 'a'}
drinks_desc = {'Gulaman': 'a', 'Buko Juice': 'a', 'Magic Water': 'a'}
menu_desc = [main_desc,side_desc,dessert_desc,drinks_desc]

questions = {
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e'
}

def randQuestion():
    key, value = random.choice(list(questions.items()))
    answer = input(f"MINIGAME QUESTION: {value}\nANSWER: ")
    return key, answer


def menuGet():
    for cat in menu:
        print()
        for item in cat:
            print(f" * {item}",end="")
        print()
        print("-"*67, end='')
    print("\n")

def clear():
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)
