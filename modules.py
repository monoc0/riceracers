import os, subprocess, random

main = ['Adobo', 'Sinigang', 'Lechon']
side = ['Lomi', 'Sopas', 'Munggo']
dessert = ['Halo-Halo', 'Taho', 'Leche Flan']
drinks = ['Gulaman', 'Buko Juice', 'Magic Water']
menu = [main,side,dessert,drinks]

main_desc = {'Adobo': 'a', 'Sinigang': 'a', 'Lechon': 'a'}
side_desc = {'Lomi': 'a', 'Sopas': 'a', 'Munggo': 'a'}
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