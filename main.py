import time

recipe = ""
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

main = ['Adobo', 'Sinigang', 'Lechon']
side = ['Lomi', 'Sopas', 'Munggo']
dessert = ['Halo-Halo', 'Taho', 'Leche flan']
drinks = ['Gulaman', 'Buko Juice', 'Magic Water']

print(title)
time.sleep(5)
user = input("Enter your username")
print(f"Welcome {user} to our program! Here you will explore the vast Filipino cuisine, and discover famous recipes and facts of Philippine cuisine!")

