# =============================================
# 🟢 LIST YARATISH BO'YICHA – 5 TA TASK
# =============================================

# Task 01: 3 ta meva nomidan iborat oddiy list
print("=" * 40)
print("Task 01: Mevalar ro'yxati")
print("=" * 40)
mevalar = ["olma", "banan", "nok"]
print(mevalar)

# Task 02: 5 ta sonli ro'yxat
print("\n" + "=" * 40)
print("Task 02: Sonlar ro'yxati")
print("=" * 40)
sonlar = [10, 20, 30, 40, 50]
print(sonlar)

# Task 03: 2 ta ro'yxat va ichma-ich list
print("\n" + "=" * 40)
print("Task 03: Ichma-ich ro'yxat")
print("=" * 40)
ismlar = ["Ali", "Vali", "Soli"]
yoshlar = [18, 20, 22]
ichma_ich = [ismlar, yoshlar]
print("Ismlar:", ichma_ich[0])
print("Yoshlar:", ichma_ich[1])
print("To'liq:", ichma_ich)

# Task 04: input() orqali 3 ta ism olish
print("\n" + "=" * 40)
print("Task 04: Foydalanuvchidan ism olish")
print("=" * 40)
# ismlar_input = []
# for i in range(3):
#     ism = input(f"{i+1}-ism kiriting: ")
#     ismlar_input.append(ism)
# print("Kiritilgan ismlar:", ismlar_input)

# Demo (input() o'rniga):
ismlar_input = ["Jasur", "Nodira", "Kamol"]  # demo uchun
print("Kiritilgan ismlar (demo):", ismlar_input)
print("(Haqiqiy ishlatish uchun yuqoridagi # ni olib tashlang)")

# Task 05: 2x2 ichma-ich ro'yxat
print("\n" + "=" * 40)
print("Task 05: 2x2 ichma-ich ro'yxat")
print("=" * 40)
matrix = [[1, 2], [3, 4]]
print("Ro'yxat:", matrix)
print("\nChiroyli ko'rinish:")
for qator in matrix:
    print(qator)
