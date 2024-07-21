#huruf besar
kata = "DICODING"
kata.lower()
print(kata)
#hurufkecil
kata ="dicoding"
kata.upper()
print(kata)
#hapus whitespace kanan string
print("dicoding       ".rstrip())
#hapus whitespace kiri string
print("           dicoding".lstrip())
#hapus whitespace kanan kiri string
print("         dicoding      ".strip())
#menghapus tertentu selain white space kanan kiri string
kata = "kodekodekodedikodingkodekode"
print(kata.strip("kode"))
#menemukan suatu kata pada awal string, output menjadi bool
print("saya sangat suka python".startswith("saya"))
#menemukan suatu kata pada akhir string, output menjadi bool
print("saya sangat suka python".endswith("python"))
#menggabungkan string
print(" ".join(["dicoding","indonesia","!"]))
#memisahkan string
print("dikoding indonesia !".split())
#memisahkan string menggunakan delimiter
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))
kata = "Ayo Belajar Pemrograman di Dikoding!"
print(kata.replace("Pemrograman", "Bahasa Python"))
#pengecekan string huruf besar
kata = "DICODING"
print(kata.isupper())
#pengecekan string huruf kecil
kata = "DICODING"
print(kata.islower())
#mengecek alphabet dalam string
kata ="DICODING"
print(kata.isalpha())
#mengecek huruf alphabet dan angka
kata ="DICODING"
print(kata.isalnum())
#mengecek angka dalam string
kata ="DICODING"
print(kata.isdecimal())
#mengecek apakah whitespace
kata = "         "
print(kata.isspace())
#mengecek apakah string berisi huruf kapital pada kata pertama
kata = "Dicoding Asik"
print(kata.istitle())
#FORMATING STRING
#Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu.
antrianke5dari100 = "5"
antrian = antrianke5dari100.zfill(3)
print(antrian)
#Metode rjust() berguna untuk merapikan pencetakan teks. Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan sehingga tampilannya lebih rapi.
print("selamat".rjust(21,"-"))
#metode ljust(), metode ini adalah kebalikan dari metode rjust() yang bertujuan untuk membuat teks menjadi rata kiri.
print("selamat".ljust(21,"-"))
#Metode center() menjadikan teks rata tengah. Metode ini akan menambahkan whitespace di sebelah kiri dan kanan secara default.
print("selamat".center(21,"-"))
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.\tseperti kata pepatah = \"pepatah \\ quotes\" ")
# Raw String Python juga menyediakan cara untuk mencetak string sesuai dengan apa pun input atau teks yang diberikan.
print(r'Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.\tseperti kata pepatah = \"pepatah \\ quotes\"')
