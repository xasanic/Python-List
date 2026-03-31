# Task 17: Foydalanuvchi istalgancha ism kiritadi (append bilan), oxirida uzunligini len() bilan chiqaring

ismlar = []
while True:
    ism = input("Ism kiriting (tugatish uchun 'stop'): ")
    if ism.lower() == "stop":
        break
    ismlar.append(ism)
print("Kiritilgan ismlar:", ismlar)
print("Jami:", len(ismlar), "ta ism")
