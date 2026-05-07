import os, subprocess, random

main = ['Adobo', 'Sinigang', 'Lechon']
side = ['Lomi', 'Sopas', 'Munggo']
dessert = ['Halo-Halo', 'Taho', 'Leche Flan']
drinks = ['Gulaman', 'Buko Juice', 'Magic Water']
menu = [main,side,dessert,drinks]

main_desc = {
    'Adobo': "Adobo, a national delicacy unique for its savory taste and pride of the Filipinos. Adobo is flavorful with its combination of soy sauce, vinegar, sugar, peppercorns, bay leaves and lots more!",
    'Sinigang': 'A sour soup usually using shrimp or pork added with tamarind, vegetables, and gabi to enhance its flavor!',
    'Lechon': 'A whole roasted pig typically served in parties or gatherings, known for its crispy skin, fatty and delicious meat! Lechon is stuffed with a multitude of herbs and spices inside the body of the pig; when cutting it open you will be hit with an array of flavorful smells!'
}

side_desc = {
    'Lomi': 'A unique dish with Chinese origin, it is a thick egg noodle soup with vegetables and pork.',
    'Sopas': 'Sopas is a creamy macaroni soup paired with hotdog and vegetables, and typically added with evaporated milk!',
    'Munggo': 'Munggo is a soup with its main ingredient being mung beans making the soft and thick texture of it. It is often cooked with onions, garlic, leaves, and shrimp!'
}

dessert_desc = {
    'Halo-Halo': 'Halo-Halo is the most popular cold dessert in the Philippines, it translates to mix-mix which is the first thing to do before consuming it. It is composed of shaved ice, evaporated milk, sweet fruits, beans, ube, cream and much more toppings that make the dessert worthwhile!',
    'Taho': 'A simple yet delicious snack, Taho is made of only soft tofu, sweet syrup, and tapioca pearls, often sold by vendors in the morning.',
    'Leche Flan': 'A sweet caramelized custard dessert, it is simply made with eggs, milk, and sugar, with its signature oval shape made from a mold called llanera.'
}

drinks_desc = {
    'Gulaman': 'Gulaman is a sweet jelly drink usually with a brown sugar syrup. It has soft and chewy agar-agar bits and tapioca pearls that make it just perfect!',
    'Buko Juice': 'Buko juice is fresh coconut water with condensed milk, shredded coconut meat, and coconut strips that are usually added to this refreshing drink!',
    'Magic Water': 'Magic Water is one of the most popular, cheap and refreshing drinks. Its magic comes from looking like plain water but having a very sweet taste. It includes water, gulaman, sugar, and banana essence!'
}

questions = {
    'Adobo': 'What is the national dish of the Philippines?',
    'Sweet': 'What is the flavor of Halo-Halo?',
    'Macaroni': 'What is the main ingredient in Sopas?',
    'Spain': 'What country heavily infulenced filipino cuisine?',
    'Lumpia': 'What do you call the filipino spring roll?'
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
