'''Topshiriq:

    Kompyuter 1 dan 100 gacha bo'lgan ixtiyoriy son o'ylasin (random kutubxonasidan foydalaning).

    Siz u sonni topishingiz kerak.

    Agar siz kichik son aytsangiz — "Kattaroq son ayting", katta son aytsangiz — "Kichikroq son ayting" deb maslahat bersin.

    Oxirida necha urinishda topganingizni ham aytsin.'''

import random

def son_game():
    tasodifiy_son = random.randint(1, 100)
    urinishlar = 0
    print(" SON TOP GAME")
    print('men 1 dan 100 gacha son uyladim topa olasanmi? ')

    while True:
        taxmin = input("\n son kiriting or exit deb yozing: ")
        if taxmin.lower() == 'exit':
            print(f"Game finished. men uylagan son {tasodifiy_son} edi ")
            break
        if not taxmin.isdigit():
            print("iltimos faqat butun son kiriting ")
            continue
        taxmin = int(taxmin)
        urinishlar += 1
        if taxmin < tasodifiy_son:
            print("xato men uylagan son katta ")
        elif taxmin > tasodifiy_son:
            print('xato men uylagan son kichik ')
        else:
            print(f"TABRIKLAYMAN {urinishlar} ta urunishda topding!!! haqiqatdan ham bu son {tasodifiy_son} edi ")
            break

son_game()

