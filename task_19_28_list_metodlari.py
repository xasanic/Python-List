# =============================================
# 🔴 LIST METODLARI BO'YICHA – 10 TA TASK
# =============================================

# Task 19: append() – yangi ism qo'shish
print("=" * 40)
print("Task 19: append()")
print("=" * 40)
ismlar = ["Ali", "Vali", "Soli"]
print("Oldin:", ismlar)
ismlar.append("Kamol")
print("Keyin:", ismlar)

# Task 20: insert() – boshiga son qo'shish
print("\n" + "=" * 40)
print("Task 20: insert()")
print("=" * 40)
sonlar = [2, 3, 4, 5]
print("Oldin:", sonlar)
sonlar.insert(0, 1)
print("Keyin:", sonlar)

# Task 21: remove() – ism o'chirish
print("\n" + "=" * 40)
print("Task 21: remove()")
print("=" * 40)
ismlar2 = ["Ali", "Vali", "Soli", "Jasur"]
print("Oldin:", ismlar2)
ismlar2.remove("Vali")
print("Keyin:", ismlar2)

# Task 22: pop() – oxirgi elementni olib tashlash
print("\n" + "=" * 40)
print("Task 22: pop()")
print("=" * 40)
ro_yxat = [10, 20, 30, 40, 50]
print("Oldin:", ro_yxat)
olingan = ro_yxat.pop()
print("Olingan element:", olingan)
print("Keyin:", ro_yxat)

# Task 23: index() – ismning indeksini aniqlash
print("\n" + "=" * 40)
print("Task 23: index()")
print("=" * 40)
ismlar3 = ["Ali", "Vali", "Soli", "Kamol"]
print("Ro'yxat:", ismlar3)
print("'Soli' ning indeksi:", ismlar3.index("Soli"))

# Task 24: count() – "Ali" necha marta qatnashgan
print("\n" + "=" * 40)
print("Task 24: count()")
print("=" * 40)
ismlar4 = ["Ali", "Vali", "Ali", "Soli", "Ali", "Kamol"]
print("Ro'yxat:", ismlar4)
print("'Ali' necha marta:", ismlar4.count("Ali"))

# Task 25: sort() – alfavit tartibida saralash
print("\n" + "=" * 40)
print("Task 25: sort()")
print("=" * 40)
mevalar = ["nok", "olma", "banan", "uzum", "gilos"]
print("Oldin:", mevalar)
mevalar.sort()
print("Keyin:", mevalar)

# Task 26: reverse() – teskari aylantirish
print("\n" + "=" * 40)
print("Task 26: reverse()")
print("=" * 40)
sonlar2 = [1, 2, 3, 4, 5]
print("Oldin:", sonlar2)
sonlar2.reverse()
print("Keyin:", sonlar2)

# Task 27: clear() – barcha elementlarni o'chirish
print("\n" + "=" * 40)
print("Task 27: clear()")
print("=" * 40)
ro_yxat2 = ["a", "b", "c", "d"]
print("Oldin:", ro_yxat2)
ro_yxat2.clear()
print("Keyin:", ro_yxat2)

# Task 28: copy() – ro'yxat nusxasini olish
print("\n" + "=" * 40)
print("Task 28: copy()")
print("=" * 40)
asl = [1, 2, 3, 4, 5]
nusxa = asl.copy()
print("Asl ro'yxat:", asl)
print("Nusxa:", nusxa)
print("Teng?", asl == nusxa)
print("Bir xil obyektmi?", asl is nusxa)

# Farqni ko'rsatish
nusxa.append(99)
print("\nNusxaga 99 qo'shildi:")
print("Asl ro'yxat:", asl)
print("Nusxa:", nusxa)
