# =============================================
# 🟡 LIST INDEXING BO'YICHA – 5 TA TASK
# =============================================

# Task 06: 5 ta shahar nomli ro'yxatdan 3-chi element
print("=" * 40)
print("Task 06: 3-chi shaharni chop etish")
print("=" * 40)
shaharlar = ["Toshkent", "Samarqand", "Buxoro", "Namangan", "Andijon"]
print("Shaharlar:", shaharlar)
print("3-chi element (index 2):", shaharlar[2])

# Task 07: Oxirgi elementni manfiy indeks bilan
print("\n" + "=" * 40)
print("Task 07: Oxirgi element (manfiy indeks)")
print("=" * 40)
mevalar = ["olma", "banan", "nok", "uzum", "shaftoli"]
print("Ro'yxat:", mevalar)
print("Oxirgi element [-1]:", mevalar[-1])

# Task 08: 2-chi elementni yangilash
print("\n" + "=" * 40)
print("Task 08: 2-chi elementni almashtirish")
print("=" * 40)
ranglar = ["qizil", "yashil", "ko'k", "sariq"]
print("Oldin:", ranglar)
ranglar[1] = "to'q sariq"
print("Keyin:", ranglar)

# Task 09: Ichma-ich listdagi elementni o'zgartirish
print("\n" + "=" * 40)
print("Task 09: Ichma-ich listda yosh o'zgartirish")
print("=" * 40)
students = [["Ali", 18], ["Vali", 20]]
print("Oldin:", students)
students[0][1] = 19  # Ali yoshini 19 ga almashtirish
print("Keyin:", students)
print("Ali ning yangi yoshi:", students[0][1])

# Task 10: Foydalanuvchi kiritgan indeksga qarab yangilash
print("\n" + "=" * 40)
print("Task 10: Indeks orqali qiymat yangilash")
print("=" * 40)
ro_yxat = ["Python", "Java", "C++", "JavaScript"]
print("Ro'yxat:", ro_yxat)
# indeks = int(input("Indeks kiriting: "))
# yangi_qiymat = input("Yangi qiymat kiriting: ")
# ro_yxat[indeks] = yangi_qiymat

# Demo:
indeks = 2
yangi_qiymat = "Rust"
ro_yxat[indeks] = yangi_qiymat
print(f"Demo: index={indeks}, yangi qiymat='{yangi_qiymat}'")
print("Yangilangan ro'yxat:", ro_yxat)
