# =============================================
# 🔵 LIST SLICING BO'YICHA – 5 TA TASK
# =============================================

# Task 11: 10 ta sondan 3-dan 6-gacha bo'lgan qism
print("=" * 40)
print("Task 11: 3-dan 6-gacha slicing")
print("=" * 40)
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("To'liq ro'yxat:", sonlar)
print("3-dan 6-gacha [2:6]:", sonlar[2:6])

# Task 12: Juft indeksdagi elementlar (0, 2, 4...)
print("\n" + "=" * 40)
print("Task 12: Juft indeksdagi elementlar")
print("=" * 40)
harflar = ["a", "b", "c", "d", "e", "f", "g"]
print("To'liq ro'yxat:", harflar)
print("Juft indekslar [::2]:", harflar[::2])

# Task 13: Ro'yxatni teskari qilish [::-1]
print("\n" + "=" * 40)
print("Task 13: Ro'yxatni teskari chiqarish")
print("=" * 40)
asl = [10, 20, 30, 40, 50]
print("Asl ro'yxat:", asl)
print("Teskari [::-1]:", asl[::-1])

# Task 14: Oxirgi 3 ta element
print("\n" + "=" * 40)
print("Task 14: Oxirgi 3 ta element")
print("=" * 40)
mevalar = ["olma", "banan", "nok", "uzum", "gilos", "o'rik"]
print("Ro'yxat:", mevalar)
print("Oxirgi 3 ta [-3:]:", mevalar[-3:])

# Task 15: Foydalanuvchidan start va end indekslari
print("\n" + "=" * 40)
print("Task 15: Start va end indeks bo'yicha slicing")
print("=" * 40)
ro_yxat = [5, 10, 15, 20, 25, 30, 35, 40]
print("Ro'yxat:", ro_yxat)
# start = int(input("Start indeks kiriting: "))
# end = int(input("End indeks kiriting: "))
# print(f"[{start}:{end}]:", ro_yxat[start:end])

# Demo:
start, end = 2, 6
print(f"Demo: start={start}, end={end}")
print(f"Natija [{start}:{end}]:", ro_yxat[start:end])
