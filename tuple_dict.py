user_db = {}   #Dictionary

def ma_lumotlarni_yigish():
    try:
        ism = input("Ismingizni kiriting: ")

        if any(char.isdigit() for char in ism):
            raise TypeError("Ismda raqam bo'lishi mumkin emas")

        yosh = int(input("Yoshingizni kiriting: "))
        
        shaxs_kalit = (ism, yosh)
        user_db[shaxs_kalit] = "Tizimga muvaffaqiyatli kirdi"
        
        print(f"Yaratilgan Tuple (Hashable): {shaxs_kalit}")
        print(f"Dictionary holati: {user_db}")
        
    except ValueError:
        print("Xato: Yosh butun son (int) bo'lishi kerak!")
    except TypeError as e:
        print(f"Xato: {e}")
    except Exception as e:
        print(f"Kutilmagan xato: {e}")
    finally:
        print("Dastur ishini yakunladi")

def chiroyli_print(ism, yosh):
    print(f"| {ism:<10} | {yosh:<3} yosh | STATUS: Aktiv |")
ma_lumotlarni_yigish()

for kalit in user_db.keys():
    # kalit bu - (ism, yosh) tupleni o'zi
    chiroyli_print(*kalit) 
