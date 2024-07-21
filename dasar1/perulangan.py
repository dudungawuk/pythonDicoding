arr = ["nasi","sayur","telur","kerupuk"]

for i in arr:
    print(i)

for i in range(1,3):
    print(f"contoh perulangan for ke {i}")

jawab = input(f'mencoba perulangan while(jawab "ya") : ')
jumlah = 0

while(jawab == "ya"):
    jumlah += 1
    jawab = input("ulang lagi tidak? : ")
