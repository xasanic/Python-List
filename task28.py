# Task 28: copy() yordamida ro'yxat nusxasini oling va ikkalasini chiqarib solishtiring

asl = [1, 2, 3, 4, 5]
nusxa = asl.copy()
print("Asl ro'yxat:", asl)
print("Nusxa:", nusxa)
print("Teng?", asl == nusxa)
print("Bir xil obyektmi?", asl is nusxa)

nusxa.append(99)
print("\nNusxaga 99 qo'shildi:")
print("Asl ro'yxat:", asl)
print("Nusxa:", nusxa)
