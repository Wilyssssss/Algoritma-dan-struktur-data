#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi / Class B
#Mata kuliah : Algoritma dan struktur data (Pak Muzaki)

#1.6 Perancangan array, struktur dan unions 

#1.) algoritma stack
#Stack
#Stack adalah struktur data dengan prinsip LIFO (Last In, First Out)
#Artinya: data yang masuk terakhir akan keluar pertama.

#Algoritma stack memiliki 4 operasi utama:
	
#-Push → menambah data ke stack
#-Pop → menghapus data paling atas
#-Peek / Top → melihat data paling atas
#-IsEmpty → mengecek apakah stack kosong

#Contoh:

#Masuk: 10, 20, 30

#Keluar: 30, 20, 10

#2.) algoritma searching
#Searching adalah proses mencari data tertentu di dalam sekumpulan data (array/list).
#Contoh:
#Mencari angka 7 di dalam data [2, 5, 7, 9, 12].

#3.) algoritma pengurutan data dasar (bubble,sorting,selection shorting dan insetion shorting)

#1. BUBBLE SORT

#Pengertian:
#Mengurutkan data dengan cara membandingkan dua data bersebelahan, lalu menukar jika salah urut. Proses diulang sampai data terurut.

data = [5, 3, 8, 4, 2]
n = len(data)

for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Hasil Bubble Sort:", data)

#2. SELECTION SORT

#Pengertian:
#Mencari data terkecil, lalu ditukar dengan data pertama, kemudian diulang untuk posisi berikutnya.

data = [5, 3, 8, 4, 2]
n = len(data)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if data[j] < data[min_index]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]

print("Hasil Selection Sort:", data)

#3. INSERTION SORT

#Pengertian:
#Mengurutkan dengan cara menyisipkan satu per satu data ke posisi yang benar seperti menyusun kartu.

data = [5, 3, 8, 4, 2]
n = len(data)

for i in range(1, n):
    key = data[i]
    j = i - 1

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = key

print("Hasil Insertion Sort:", data)

#4.) algoritma pengurutan data tingkat lanjut (algoritma shell sort, merge sort dan quict sort)

#1. SHELL SORT
#Pengertian
#Shell Sort adalah pengembangan dari Insertion Sort dengan membandingkan data yang berjauhan lebih dulu, lalu jaraknya diperkecil sampai 1.

data = [8, 3, 7, 4, 9, 2]
n = len(data)
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        temp = data[i]
        j = i
        while j >= gap and data[j - gap] > temp:
            data[j] = data[j - gap]
            j -= gap
        data[j] = temp
    gap //= 2

print("Hasil Shell Sort:", data)

#2. MERGE SORT
#Pengertian
#Merge Sort menggunakan metode Divide and Conquer:
#Data dibagi dua
#Diurutkan masing-masing
#Digabung kembali secara terurut

def merge_sort(data):
    if len(data) > 1:
        tengah = len(data) // 2
        kiri = data[:tengah]
        kanan = data[tengah:]

        merge_sort(kiri)
        merge_sort(kanan)

        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1

data = [8, 3, 7, 4, 9, 2]
merge_sort(data)
print("Hasil Merge Sort:", data)

#3. QUICK SORT
#Pengertian
#Quick Sort juga memakai Divide and Conquer, dengan memilih pivot, lalu membagi data menjadi:
#-Lebih kecil dari pivot
#-Lebih besar dari pivot

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    kiri = [x for x in data if x < pivot]
    tengah = [x for x in data if x == pivot]
    kanan = [x for x in data if x > pivot]
    return quick_sort(kiri) + tengah + quick_sort(kanan)

data = [8, 3, 7, 4, 9, 2]
hasil = quick_sort(data)
print("Hasil Quick Sort:", hasil)

# Tambahan
#Arti Pseudocode adalah:
#Pseudocode adalah cara menuliskan langkah-langkah algoritma dengan bahasa sederhana yang mirip bahasa manusia dan pemrograman, tetapi bukan bahasa program yang sebenarnya (tidak bisa langsung dijalankan di komputer).