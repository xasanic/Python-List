# =============================================
# 🟠 LIST LEN() BO'YICHA MANTIQIY – 3 TA TASK
# =============================================

# Task 16: Uzunlik aniqlash va shartli tekshirish
print("=" * 40)
print("Task 16: Ro'yxat uzunligi tekshirish")
print("=" * 40)
ro_yxat = [1, 2, 3, 4, 5, 6]
uzunlik = len(ro_yxat)
print("Ro'yxat:", ro_yxat)
print("Uzunlik:", uzunlik)
if uzunlik > 5:
    print("Ko'p element")
else:
    print("Kam element")

# Task 17: append bilan ism qo'shish, uzunligini chiqarish
print("\n" + "=" * 40)
print("Task 17: Foydalanuvchi ism kiritadi")
print("=" * 40)
ismlar = []
# while True:
#     ism = input("Ism kiriting (tugatish uchun 'stop'): ")
#     if ism.lower() == "stop":
#         break
#     ismlar.append(ism)
# print("Kiritilgan ismlar:", ismlar)
# print("Jami:", len(ismlar), "ta ism")

# Demo:
demo_ismlar = ["Ali", "Vali", "Soli", "Kamol"]
for ism in demo_ismlar:
    ismlar.append(ism)
print("Kiritilgan ismlar (demo):", ismlar)
print("Jami:", len(ismlar), "ta ism")

# Task 18: Uzunlik toq yoki juft
print("\n" + "=" * 40)
print("Task 18: Uzunlik toq yoki juft")
print("=" * 40)
ro_yxat1 = [1, 2, 3, 4, 5]      # toq
ro_yxat2 = [1, 2, 3, 4]         # juft

for r in [ro_yxat1, ro_yxat2]:
    uzunlik = len(r)
    if uzunlik % 2 != 0:
        print(f"Ro'yxat {r} → uzunlik {uzunlik} → True (toq)")
    else:
        print(f"Ro'yxat {r} → uzunlik {uzunlik} → False (juft)")
