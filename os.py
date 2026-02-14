# import os
# print(os.getcwd())
# # print(os.chdir('/home/ozod/Desktop/heropy'))
# print(os.listdir())
# print(os.path.exists('path'))
# os.chdir('/home/ozod/Downloads')
import os
import time

# DEKORATOR
#dekaratorlar funksiyani uzgartirmasdan uning ustiga yangi func lar qushish uchun ishlatiladi 
# vaqt funcsiyasini boshqa funcs ustiga yozdim

downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
def vaqt(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"sarflangan vaqt = {end - start: 4f} soniya")
        return result
    return wrapper

@vaqt
def filesearch(papka):
    for fayl in os.listdir(papka):
        if fayl.endswith('.doc') or fayl.endswith('.docx'): #endswith oxiri shu bilan tugagan filelar qidiradi
            yield os.path.join(papka, fayl) 
# GENERATOR 
#generator filelar kup bulsa (masalan 1 mlnta ) ram tulmasligi uchun 1 tadan file ni topib 2 func ga chiqarib beradi (yield yordamida) 
@vaqt
def filedel(papka):
    count = 0
    for fayl_yoli in filesearch(papka):
        try:
            os.remove(fayl_yoli) # asosiy func
            print(f"O'chirildi: {os.basename(fayl_yoli)}")
            count += 1
        except Exception as e:
            print(f"Xato yuz berdi ({fayl_yoli}): {e}")
    
    print(f"\nJami {count} ta hujjat o'chirildi.")

filedel(downloads_path)

