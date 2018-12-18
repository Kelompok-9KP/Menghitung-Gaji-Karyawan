print ("=========================================")
print ("      Aplikasi Penggajian Karyawan")
print ("=========================================")

nama = str(input("nama pegawai :"))
tingaktan = str(input("tingkatan :"))
awal = int(input("tahun awal bekerja :"))
akhir = int(input("habis kontrak :"))
gapok = int(input("gaji pokok :"))
jam = int(input("jmlh jam bekerja :"))
hari = int(input("jmlh hari bekerja :"))
anak = int(input("jmlh anak :"))
kerja = 9+jam 
tgb = (gapok/hari*jam)+(anak*50000)
tgt = tgb*12
tga = tgt*(akhir-awal)

if golongan == "A":
	print("jabatan = Direktur")
elif golongan == "B":
	print("Jabatan = Manager")
elif golongan == "C":
	print("Jabatan = Superviser")
elif golongan == "D":
	print("Jabatan = Operator")

if anak < 1:
  print ("Jomblo akut")
elif anak == 1:
  print ("Baru Menikah")
elif anak > 1:
  print("Sudah Menikah")
  
print ("\n\n=============================")
print ("\nNama pegawai					: ",nama)
print ("mulai kerja					: ",awal)
print ("akhir kerja					: ",akhir)
print ("jam kerja					:  9 s/d ",kerja)
print ("perbulan					: Rp. ",tgb)
print ("pertahun					: Rp. ",tgt)
print ("total gaji diterima adalah			: Rp. ",tga)
print ("")