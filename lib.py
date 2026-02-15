'''"Kutubxona boshqaruvi"
Sizda kitoblar ro'yxati (list) bor. Har bir kitob esa lug'at (dictionary) ko'rinishida:
Vazifa:

    Foydalanuvchidan yil kiritishini so'rang (masalan: 1950).

    Ro'yxatdan shu yildan keyin chop etilgan kitoblarni topib, ekranga chiqaring.

    Agar bunday kitob topilmasa, "Hech narsa topilmadi" deb xabar bering.'''

books = [
    {"title": "O'tkan kunlar", "author": "Abdulla Qodiriy", "year": 1920},
    {"title": "Sariq devni minib", "author": "Xudoyberdi To'xtaboyev", "year": 1968},
    {"title": "Yulduzli tunlar", "author": "Pirimqul Qodirov", "year": 1978}
]

while True:
    search = input('\nKitob yilini kiriting (masalan: 1950) yoki "exit" deb yozing: ')
    
    if search.lower() == 'exit':
        break
        
    if not search.isdigit() or len(search) != 4:
        print("Iltimos, 4 raqamli butun son kiriting!")
        continue

    yil_chegarasi = int(search)
    topilganlar = []

    for kitob in books:
        if kitob["year"] >= yil_chegarasi:
            topilganlar.append(kitob)

    if topilganlar:
        print(f"\n{yil_chegarasi} yildan keyin chop etilgan kitoblar:")
        for k in topilganlar:
            print(f"- {k['title']} ({k['author']}), yili: {k['year']}")
    else:
        print(f"\n{yil_chegarasi} yildan keyin chop etilgan kitoblar topilmadi.")
    
    break 
