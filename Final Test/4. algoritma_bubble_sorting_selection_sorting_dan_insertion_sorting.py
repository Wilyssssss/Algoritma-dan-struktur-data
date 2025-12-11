#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi clas b
#Matkul : Algoritma dan struktur data ( UAS )

#1. Bubble Sort
#Cara kerja: Membandingkan pasangan elemen berurutan, menukar jika urutan salah, hingga seluruh data terurut.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

data = [90, 99, 97, 95, 93]
bubble_sort(data)
print("Bubble Sort:", data)

#2. Selection Sort
#Cara kerja: Mencari elemen terkecil (atau terbesar) dari sisa list, lalu menukarnya dengan posisi awal yang belum terurut.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

data = [1000, 999, 888, 777, 666]
selection_sort(data)
print("Selection Sort:", data)

#3. Insertion Sort
#Cara kerja: Memasukkan setiap elemen ke posisi yang tepat di bagian list yang sudah terurut.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

data = [111, 222, 333, 444, 555]
insertion_sort(data)
print("Insertion Sort:", data)
