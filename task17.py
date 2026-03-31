ismlar = []

while True:
    ism = input("Ism kiriting (stop - tugatish): ")
    if ism == "stop":
        break
    ismlar.append(ism)

print(ismlar)
print("Jami:", len(ismlar))
