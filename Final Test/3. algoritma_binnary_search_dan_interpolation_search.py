#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi clas b
#Matkul : Algoritma dan struktur data ( UAS )

# Binary Search
# Binary Search adalah algoritma pencarian pada array yang sudah terurut (ascending atau descending). Ia bekerja dengan cara membagi dua bagian, lalu menentukan apakah data yang dicari berada di kiri atau kanan bagian tengah.
#contoh

def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid 
        elif target < data[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1  

nama = ["william", "alim", "naufal", "masriadi", "mahmud", "sandry"]
target = "masriadi"

hasil = binary_search(nama, target)
print("Ditemukan pada indeks:",target, hasil)

# Interpolation Search
# Interpolation Search mirip Binary Search tapi titik tengahnya tidak selalu di tengah, melainkan diperkirakan berdasarkan nilai target.Interpolation Search sebenarnya paling cocok untuk angka, karena perhitungan posisi estimasi berdasarkan nilai numerik.
def interpolation_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right and target >= data[left] and target <= data[right]:
        if left == right:
            if data[left] == target:
                return left
            return -1

        pos = left + ((target - data[left]) * (right - left)) // (data[right] - data[left])

        if data[pos] == target:
            return pos
        elif target < data[pos]:
            right = pos - 1
        else:
            left = pos + 1

    return -1


angka = [10, 20, 30, 40, 50, 60, 70, 80]
target = 30

hasil = interpolation_search(angka, target)
print("Ditemukan pada indeks:",target, hasil)
