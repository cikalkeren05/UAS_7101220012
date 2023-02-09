# * Input User
phonebook = input("Enter your phone number: ")
print(phonebook)
print(type(phonebook))

print("\nGet Integer Output")
phonebook = int(input("Enter your phone number: "))
print(phonebook)
print(type(phonebook))

print("\nGet Float Output")
phonebook = float(input("Enter number: "))
print(phonebook)
# print(type(phonebook))
print(f"Tipe data dari variabel 'phonebook' adalah: {type(phonebook)}")

# TODO 1 : Coding Exercise Check-in: Python User Input
# ? TASK : Buatlah program yang dapat menghitung kecepatan dan waktu tempuh suatu mobil
# ? -> dengan detail sebagai berikut:
# ? * variabel : kecepatan, waktu, dan jarak
# ? * output : Kecepatan rata-rata(km/jam) : <kecepatan>
# ? * output : Waktu tempuh (jam) : <waktu>
# ? * output : Jarak tempuh : <kecepatan> * <waktu> = <jarak> km

# * Your Code Goes Here


# TODO 2 : Coding Exercise Check-in: Python User Input
# ? Sebuah operator "XYZ" paca bayar menerapkan tarif service sebegai berikut:
# ? - Percakapan = Rp. 1000/menit,
# ? - SMS = Rp. 300/sms,
# ? - Abodemen = Rp. 20000/bulan
# ? TASK : Buatlah program menghitung besar tagihan telepon dengan Input:
# ? * variabel : nama, cakap, SMS
# ? TITLE : DATA PELANGGAN
# ? * output : Nama Pelanggan : <nama>
# ? * output : Percakapan : <cakap> menit
# ? * output : SMS : <sms> kali
# ? TITLE : TAGIHAN
# ? * output : Abodemen : <abn>
# ? * output : Biaya Percakapan : <rp_cakap>
# ? * output : Biaya SMS : <rp_sms>
# ? * output : Total Tagihan : <t_tagih>

# * Your Code Goes Here

kecepatan = float(input("Masukkan kecepatan mobil (km/jam): "))
waktu = float(input("Masukkan waktu tempuh (jam): "))
jarak = kecepatan * waktu

kecepatan_rata = jarak / waktu

print("Kecepatan rata-rata (km/jam): ", kecepatan_rata)
print("Waktu tempuh (jam): ", waktu)
print("Jarak tempuh: ", jarak, "km")

print("\n --Menghitung Besar Tagihan Telepon Dan Sms Pelanggan--")

nama = input("Masukkan nama pelanggan: ")
cakap = float(input("Masukkan jumlah menit percakapan: "))
sms = float(input("Masukkan jumlah SMS: "))

# Tarif
cakap_rate = 1000
sms_rate = 300
abn = 20000

# Hitung biaya
rp_cakap = cakap * cakap_rate
rp_sms = sms * sms_rate
t_tagih = abn + rp_cakap + rp_sms

# Output hasil perhitungan
print("\n--- DATA PELANGGAN ---")
print("Nama Pelanggan: ", nama)
print(f"Durasi Percakapan: {int(cakap)} menit")
print(f"Jumlah SMS:  {int(sms)} kali")

print("\n--- TAGIHAN ---")
print("Abodemen: Rp.", abn)
print("Biaya Percakapan: Rp.", rp_cakap)
print("Biaya SMS: Rp.", rp_sms)
print("Total Tagihan: Rp.", t_tagih)