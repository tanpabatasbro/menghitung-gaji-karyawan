print(f"{'PROGRAM MENGHITUNG GAJI KARYAWAN':^60}")
print(f"{'='*60:^60}")

nama = input("Masukkan Nama :")
lama_lembur = int(input("Masukkan Lama Lembur"))
gaji_pokok = 5000000
lembur_perjam = 55000
pajak = 10/100
gaji_lembur = lembur_perjam  * lama_lembur
gaji_kotor = gaji_pokok + gaji_lembur
potongan = gaji_kotor * pajak
gaji_bersih = gaji_kotor - potongan

print(f"{'='*60:^60}")
print(f"{'GAJI KARYAWAN':^60}")
print(f"{'='*60:^60}")

print(f"Nama\t\t :{nama}")
print(f"Gaji Pokok\t :{gaji_pokok}")
print(f"Bonus Lembur/Jam :{lembur_perjam}")
print(f"Potongan Pajak\t :10%")
print(f"Gaji Kotor\t :{gaji_kotor}")
print(f"Gaji Bersih\t :{gaji_bersih}")
