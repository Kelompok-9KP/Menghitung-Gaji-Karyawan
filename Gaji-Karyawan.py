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

if anak < 1:
  print ("Jomblo akut")
elif anak == 1:
  print ("Baru Menikah")
elif anak > 1:
  print("Sudah Menikah")
  
print ("\n\n=============================")
  