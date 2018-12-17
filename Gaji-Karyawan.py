print ("=========================================")
print ("      Aplikasi Penggajian Karyawan")
print ("=========================================")

nama = str(input("nama pegawai :"))
golongan = str(input("golongan :"))
awal = int(input("tahun awal bekerja :"))
akhir = int(input("habis kontrak :"))
gapok = int(input("gaji pokok :"))
jam = int(input("jam per hari bekerja :"))
hari = int(input("jmlh hari bekerja :"))
anak = int(input("jmlh anak :"))
kerja = 9+jam 
tgb = (hari*jam)*(anak*25000)
tgt = tgb*12
tga = tgt*(akhir-awal)

if Golongan == "A":
	print("jabatan = Direktur")
elif Golongan == "B":
	print("Jabatan = Manager")
elif Golongan == "C":
	print("Jabatan = Superviser")
elif Golongan == "D":
	print("Jabatan = Operator")

if anak < 1:
  print ("Jomblo akut")
elif anak == 1:
  print ("Baru Menikah")
elif anak > 1:
  print("Sudah Menikah")
  
print ("\n\n=============================")