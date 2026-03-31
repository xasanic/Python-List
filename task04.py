# Task 04: input() yordamida foydalanuvchidan 3 ta ism olib ro'yxat yarating

ismlar = []
for i in range(3):
    ism = input(f"{i+1}-ism kiriting: ")
    ismlar.append(ism)
print("Kiritilgan ismlar:", ismlar)
