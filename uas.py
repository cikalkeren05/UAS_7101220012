# input
omset = int (input("masukan omset penjualan:  "))
tpengeluaran = int (input("masukan total pengeluaran perusahaan:  "))

# proses
keuntungan = omset - tpengeluaran
ali = keuntungan * 20 / 100
budi = keuntungan * 30 / 100 
susi = keuntungan * 50 / 100

# output
print("keuntungan ali:", ali)
print("keuntungan budi:", budi)
print("keuntungan susi:", susi) 