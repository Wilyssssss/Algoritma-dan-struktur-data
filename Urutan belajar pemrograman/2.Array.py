#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi / Class B
#Mata kuliah : Algoritma dan struktur data (Pak Muzaki)

#1.2 Tipe data Array satu dimensi, dua dimensi, dan tiga dimensi : 

#Pengrtian Array, Array dalam pemrograman Python adalah struktur data yang menyimpan koleksi elemen bertipe data sama dalam lokasi memori yang berurutan.

#1.) Tipe data Array satu dimensi
# Array satu dimensi adalah array yang hanya memiliki satu baris data atau satu daftar elemen. Biasanya digunakan untuk menyimpan kumpulan data sejenis dalam satu variabel. contoh :

nilai = [80, 85, 90, 95]
print(nilai[0])   # Output: 80
print(nilai[2])   # Output: 90

#.2) Tipe data array dua dimensi
# Array dua dimensi adalah array yang memiliki baris dan kolom, seperti tabel atau matriks. contoh :

angka = [
    [1, 2, 3],
    [4, 5, 6]
]

print(angka[0][1])  # Output: 2
print(angka[1][2])  # Output: 6

#3.) Tipe data array tiga dimensi
# Array tiga dimensi adalah array yang memiliki lapisan, baris, dan kolom. Bisa dianggap sebagai kumpulan beberapa array 2 dimensi.

data = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print(data[0][1][1])  # Output: 4
print(data[1][0][0])  # Output: 5
