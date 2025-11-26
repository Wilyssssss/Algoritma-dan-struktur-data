#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi / Class B
#Tugas dari Bapak Muzaki

import pygame   #Library untuk membuat game (grafik, input mouse, dll)
import sys      #Untuk keluar dari program dengan aman (sys.exit)
import time     #Untuk memberikan jeda waktu (sleep)
import os       #Untuk mengatur lokasi file (path gambar)

#Inisialisasi semua modul pygame
pygame.init()

#BACKGROUND
#Mengambil lokasi folder tempat file Python berada
base_path = os.path.dirname(__file__)

#Menggabungkan folder dengan nama file gambar
bg_path = os.path.join(base_path, "Gambar_william_pemandangan.jpg")

#Memuat gambar background
background = pygame.image.load(bg_path)

#Mengubah ukuran background sesuai ukuran layar
background = pygame.transform.scale(background, (300, 350))

#UKURAN
WIDTH, HEIGHT = 300, 350     # Ukuran layar
LINE_WIDTH = 5              # Tebal garis papan
SQUARE_SIZE = WIDTH // 3    # Ukuran tiap kotak (300 : 3 = 100)

#WARNA
LINE_COLOR = (255, 255, 255)      # Warna garis putih
X_COLOR = (255, 255, 255)         # Warna simbol X
O_COLOR = (255, 255, 255)         # Warna simbol O
WIN_LINE_COLOR = (255, 255, 255)  # Warna garis kemenangan

#LAYAR
#Membuat jendela game
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)

#Memberi judul pada window game
pygame.display.set_caption("TicTacToe By William")

#FONT LEBIH HD
#Membuat font untuk tampilan score
font = pygame.font.SysFont("Arial", 40, bold=True)

#SCORE
score_x = 0   # Nilai score pemain X
score_o = 0   # Nilai score pemain O

#PAPAN
#Membuat papan 3x3 yang berisi angka 0
board = [[0 for _ in range(3)] for _ in range(3)]

player = 1        # Player 1 = X, Player 2 = O
game_over = False  # Status game selesai atau belum
win_line = None    # Menyimpan posisi garis kemenangan

#DRAW
def draw_lines():
    """Menggambar semua garis papan dan garis pemisah score"""
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (WIDTH, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (WIDTH, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 300), (WIDTH, 300), 5)  # Garis di atas score
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)

def draw_score():
    """Menampilkan score pemain X dan O"""
    bg_surface = pygame.Surface((WIDTH, 45), pygame.SRCALPHA)
    bg_surface.fill((0, 0, 0, 0))  # Background transparan
    screen.blit(bg_surface, (0, 0))

    # Membuat teks score
    text = font.render(f"X: {score_x}   O: {score_o}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, 327))

    # Menampilkan teks score ke layar
    screen.blit(text, text_rect)

def draw_figures():
    """Menggambar simbol X dan O di papan"""
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:  # Jika isi 1, gambar X
                pygame.draw.line(screen, X_COLOR,
                                 (col * 100 + 20, row * 100 + 20),
                                 (col * 100 + 80, row * 100 + 80), 5)
                pygame.draw.line(screen, X_COLOR,
                                 (col * 100 + 20, row * 100 + 80),
                                 (col * 100 + 80, row * 100 + 20), 5)

            elif board[row][col] == 2:  # Jika isi 2, gambar O
                pygame.draw.circle(screen, O_COLOR,
                                   (col * 100 + 50, row * 100 + 50),
                                   35, 5)

def draw_win_line():
    """Menggambar garis kemenangan jika ada yang menang"""
    if win_line:
        pygame.draw.line(screen, WIN_LINE_COLOR, win_line[0], win_line[1], 8)

#LOGIC
def mark_square(row, col, player):
    """Mengisi kotak dengan angka player (1 atau 2)"""
    board[row][col] = player

def available_square(row, col):
    """Mengecek apakah kotak masih kosong"""
    return board[row][col] == 0

def check_win(player):
    """Mengecek apakah player menang"""
    global win_line

    #Cek semua baris
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            win_line = ((0, row * 100 + 50), (WIDTH, row * 100 + 50))
            return True

    #Cek semua kolom
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            win_line = ((col * 100 + 50, 0), (col * 100 + 50, 300))
            return True

    #Cek diagonal kiri atas ke kanan bawah
    if board[0][0] == board[1][1] == board[2][2] == player:
        win_line = ((0, 0), (300, 300))
        return True

    #Cek diagonal kanan atas ke kiri bawah
    if board[0][2] == board[1][1] == board[2][0] == player:
        win_line = ((300, 0), (0, 300))
        return True

    return False

def restart():
    """Mereset papan setelah game selesai"""
    global board, player, game_over, win_line
    time.sleep(1)  # Jeda 1 detik sebelum reset
    screen.blit(background, (0, 0))
    draw_lines()
    board = [[0 for _ in range(3)] for _ in range(3)]  # Kosongkan papan
    player = 1
    game_over = False
    win_line = None

#MAIN LOOP
while True:
    #Menampilkan background
    screen.blit(background, (0, 0))

    #Menggambar garis papan
    draw_lines()

    #Membaca semua event (mouse, quit, dll)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Menutup pygame
            sys.exit()     # Keluar dari program

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos  # Ambil posisi klik mouse

            if mouseY < 300:
                row = mouseY // 100     # Menentukan baris yang diklik
                col = mouseX // 100     # Menentukan kolom yang diklik

                if available_square(row, col):
                    mark_square(row, col, player)

                    if check_win(player):
                        game_over = True
                        if player == 1:
                            score_x += 1
                        else:
                            score_o += 1

                    #Ganti giliran pemain
                    player = 2 if player == 1 else 1

    #Menggambar X dan O
    draw_figures()

    #Menggambar garis kemenangan
    draw_win_line()

    #Menampilkan score
    draw_score()

    #Jika game selesai, reset
    if game_over:
        pygame.display.update()
        restart()

    #Update tampilan layar setiap frame
    pygame.display.update()

#TAMBAHAN KATA DARI WILLIAM OKTA JAYA
    #gamenya akan langsung berhenti jika draw, dan gamenya harus dibuka lagi, kalo win bakalan lanjut terus.
    #Jangan lupa fotonya untuk digabungkan ke dalam folder yang sama agar tidak error.
