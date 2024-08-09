import tkinter as tk

# Fungsi untuk menambahkan teks ke layar kalkulator
def tambah_angka(angka):
    layar_kalkulator.insert(tk.END, angka)

# Fungsi untuk menghitung hasil ekspresi matematika
def hitung():
    try:
        hasil = eval(layar_kalkulator.get())
        layar_kalkulator.delete(0, tk.END)
        layar_kalkulator.insert(tk.END, hasil)
    except:
        layar_kalkulator.delete(0, tk.END)
        layar_kalkulator.insert(tk.END, "Error")

# Fungsi untuk menghapus layar kalkulator
def hapus():
    layar_kalkulator.delete(0, tk.END)

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator")

# Membuat layar kalkulator
layar_kalkulator = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
layar_kalkulator.grid(row=0, column=0, columnspan=4)

# Membuat tombol-tombol angka dan operasi
tombol = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Menempatkan tombol-tombol pada grid
baris = 1
kolom = 0

for simbol in tombol:
    if simbol == "=":
        tombol_buat = tk.Button(root, text=simbol, padx=40, pady=20, font=("Arial", 18), command=hitung)
    else:
        tombol_buat = tk.Button(root, text=simbol, padx=40, pady=20, font=("Arial", 18), command=lambda simbol=simbol: tambah_angka(simbol))
    tombol_buat.grid(row=baris, column=kolom)

    kolom += 1
    if kolom > 3:
        kolom = 0
        baris += 1

# Tombol hapus
tombol_hapus = tk.Button(root, text="C", padx=40, pady=20, font=("Arial", 18), command=hapus)
tombol_hapus.grid(row=baris, column=0, columnspan=4)

# Menjalankan aplikasi
root.mainloop()
