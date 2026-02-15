'''1. "Aqlli" Parol Tekshirgich (Sodda)

Foydalanuvchidan parol kiritishni so'rang va u quyidagi shartlarga javob berishini tekshiring:

    Uzunligi kamida 8 ta belgidan iborat bo'lsin.

    Tarkibida kamida bitta son bo'lsin.

    Tarkibida kamida bitta katta harf bo'lsin.'''


parol = (input("parolni kiriting: "))

uzunlik = len(parol) >= 8
katta_harf = any(char.isupper() for char in parol)
son = any(char.isdigit() for char in parol)

if uzunlik and katta_harf and son:
    print("tugri parol")
else:
    print('Xato parol ')
    if not uzunlik:
        print('8 ta belgi bulishi kk ')
    if not katta_harf:
        print('kamida bitta katta harf kk')
    if not son:
        print('kamida bitta son kerak ')
        
