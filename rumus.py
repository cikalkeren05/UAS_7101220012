# input
kehadiran = float(input("masukkan nilai kehaadiran (0-100): "))
tugas = float(input("masukkan nilai tugas (0-100): "))
uts = float(input("masukkan nilai uts (0-100): "))
uas = float(input("masukkan nilai uas (0-100): "))

# proses
na = 0.1 * kehadiran + 0.2 * tugas + 0.3 * uts + 0.4 * uas
if na >= 85:
    grade = "A"
elif na >= 70:
    grade = "B"
elif na >= 55:
    grade = "C"
elif na >= 40:
    grade = "D"
else:
    grade = "E"

# output
print("nilai akhir:", na)
print("grade:", grade)
80