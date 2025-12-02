#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi / Class B
#Mata kuliah : Algoritma dan struktur data (Pak Muzaki)

#1.5 Variabel statis dan variabel dinamis : 

#Variabel statis dalam Python biasanya dimaknai sebagai variabel yang tipe datanya dibuat tetap menggunakan type hint (anotasi tipe) atau variabel yang nilainya tidak berubah selama program berjalan.

#Variabel dinamis dalam Python adalah variabel yang tipe datanya bisa berubah-ubah secara otomatis selama program berjalan tanpa harus dideklarasikan terlebih dahulu.

#contoh
#variabel statis
PI = 3.14   # variabel statis (konstanta)

r = 7
luas = PI * r * r

print("Jari-jari:", r)
print("Luas lingkaran:", luas)

#variabel dinamis
nilai = 10
print("Nilai awal:", nilai)

nilai = 20
print("Nilai setelah diubah:", nilai)

nilai = nilai + 5
print("Nilai akhir:", nilai)
