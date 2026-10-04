import time
name = input("isming nima? ")
time.sleep(2)
print("hush kebsan " + name)
time.sleep(2)
birth_year = input("qaysi yili tugilgansan: ")
time.sleep(2)
age = 2026 - int(birth_year)
time.sleep(2)
print("Sen " + str(age) + " yoshdasan.")
time.sleep(2)
first = input("hohlagan raqam yoz: ")
time.sleep(2)
second = input("yana boshqa raqam yoz: ")
time.sleep(2)

sum = float(first) + float(second)
time.sleep(2)

print("jami qo'shilganda: " + str(sum))
time.sleep(2)
while True:
    temp_input = input("Hozir yashayotgan joyingda nechi gradus issiq? ")
    time.sleep(2)
    
    # Son kiritilganini tekshirish (matn kiritilsa xato beradi)
    time.sleep(2)
    if temp_input.replace('.', '', 1).isdigit():
        temperature = float(temp_input)
        break  # To'g'ri son kiritilsa, so'rashni to'xtatadi
    else:
        print("faqat raqam yoz!")
        time.sleep(2)

# Shartlarni tekshirish va javob qaytarish
if temperature < 25:
    print("koreadan sovuqroq ekan!")
    time.sleep(2)
elif temperature >= 30:
    print("issiq ekan,qorayib ket.")
    time.sleep(2)
else:
    print("unchalik issiqmas ekan kochaga chiqib yugurib kel!")
    time.sleep(2)
import time

while True:
    ism = input("O'zbekiston Respublikasi Prezidentining ism va familiyasini yoz: ")
    time.sleep(2)
    
    # .upper() yordamida kiritilgan matnni butunlay KATTA harflarga o'tkazib tekshiramiz
    if ism.upper() == "SHAVKAT MIRZIYOYEV":
        print("\nyaxshi! 🌟")
        break
    else:
        print("Shuniyam bilmaysanmi? Qaytadan urinib ko'r! ❌\n")

# To'g'ri topgandan keyin ko'rsatiladigan zo'r narsa (Animatsiya)
print("to'g'ri topganing uchun maxsus sovg'a tayyorlanmoqda...")
time.sleep(2) # 2 soniya kutib turadi

print("\n🔥 MANA SENGA SOVG'A: RAKETA! 🔥\n")
time.sleep(1)

# Raketa uchish animatsiyasi
for i in range(5, 0, -1):
    print(f"hozir boshlanadi: {i}...")
    time.sleep(1)

print("\n🚀")
print("    /\\")
print("   /  \\")
print("  |    |")
print("  |    |")
print(" /|    |\\")
print("/_|_  _|_\\")
print("   |  |")
print("   |  |")
print("  /____\\")
print("  vvvvvv")
print(" 🔥🔥🔥🔥🔥")
print("\nbarakalla! 🏆")
print("yana nima qilsam ekan🤔")
time.sleep(3)
