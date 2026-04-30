import os, subprocess

main = ['Adobo', 'Sinigang', 'Lechon']
side = ['Lomi', 'Sopas', 'Munggo']
dessert = ['Halo-Halo', 'Taho', 'Leche Flan']
drinks = ['Gulaman', 'Buko Juice', 'Magic Water']
menu = [main,side,dessert,drinks]

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