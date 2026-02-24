# create def 


while True:
    parol_str = input("4 xonali parol kiriting: ") 
    
    if len(parol_str) == 4 and parol_str.isdigit():
        parol = int(parol_str) 
        print("Parol muvaffaqiyatli o'rnatildi!")
        break
    else:
        print("Xato! Iltimos, aynan 4 ta RAQAM kiriting.")

# 2. Parolni topish funksiyasi
def paroltop(asl_parol):
    found = False
    for hak in range(1000, 10000): # 9999 gacha tekshirish uchun 10000 yoziladi
        if hak == asl_parol:
            print(f"Parol topildi! U {hak} ga teng.")
            found = True
            break
    
    if not found:
        print("Parol berilgan diapazondan topilmadi.")

# Funksiyani chaqirish
paroltop(parol)