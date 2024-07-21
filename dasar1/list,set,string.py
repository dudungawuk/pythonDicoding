# Fungsi len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string. Khusus pada string, program akan menghitung jumlah karakternya.
contoh_list = [1,2,3,4,5,6,7,8]
kata = "dicoding"
panjang = contoh_list

print(len(contoh_list))
print(len(kata))

#nilai minimum dan maksimum dari suatu list menggunakan fungsi min() dan max().
contoh_list = [32,45,54,7,3,76,4,66,10]
print(max(contoh_list))
print(min(contoh_list))

#Fungsi count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.

contoh_list = [4,5,6,5,6,5,5,4,5,5]
print(contoh_list.count(5))
# In dan not in merupakan operator yang diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list.
kalimat = "belajar python sangat seru yaaaa!"
print("dicoding"in kalimat)
print("python"in kalimat)
print("dicoding"not in kalimat)
print("python"not in kalimat)
# memberikan nilai untuk multiple variable dalam list

contoh_list = ["fikri",22,"python dev"]
# nama = contoh_list[0]
# umur = contoh_list[1]
# keahlian = contoh_list[2]
nama,umur,keahlian = contoh_list

print(contoh_list)
print(nama)
print(umur)
print(keahlian)

# Anda bisa menggunakan fungsi sort() untuk mengurutkan angka atau urutan huruf.
#Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya.'
#Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
list_string = ["Bebek","Ayam","Cicak","angsa"]
list_num = [32,45,54,7,3,76,4,66,10]
list_num.sort(reverse=True)
list_string.sort()
print(list_num)
print(list_string)
