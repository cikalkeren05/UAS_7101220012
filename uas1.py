 # Input
gaji = int(input("masukkan gaji: "))
hutang = int(input("masukkan hutang: "))

 # proses
keuangan = gaji - hutang
biaya_sehari_hari = keuangan * 70 / 100
tabungan = keuangan * 20 / 100
infak = keuangan - biaya_sehari_hari - tabungan

 # output
print("biaya sehari-hari:", biaya_sehari_hari)
print("tabungan:", tabungan) 
print("infak:", infak)
