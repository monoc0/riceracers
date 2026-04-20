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

menu = ['Adobo', 'Pancit', 'Sinigang', 'Lechon', 'Tinola', 'Kaldereta', 'Kare Kare', 'Arroz Caldo', 'Lumpia', 'Bulalo', 'Bicol express', 'Tapsilog', 'Lomi', 'Bistek Beef'
]
dessert = ['Bibingka', 'Halo-Halo', 'Taho', 'Champarado(tm)', 'Leche flan', 'Mango float']

time.sleep(5)
print(title)
time.sleep(5)
user = input("Enter your username")
print(f"Welcome {user} to our program! Here you will explore the vast Filipino cuisine, and discover famous recipes and facts of Philippine cuisine!")
