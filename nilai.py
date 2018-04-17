print "PROGRAM NILAI AKHIR MAHASISWA"
print "Anggata Amelia"
print "311710085"

print "#################################################"
print "**********NILAI MATA KULIAH PROGRAMMING**********"
print "#################################################"

nama =raw_input("Masukkan Nama    :")
uts =input("Masukkan Nilai UTS    :")
uas =input("Masukkan Nilai Uas    :")
tgs =input("Masukkan Nilai Tugas  :")
print "NAMA        : %s"%nama
print "Nilai UTS   : %d"%uts
print "Nilai UAS   : %d"%uas
print "Nilai Tugas : %d"%tgs

nilai = (( uts + uas + tgs )/3)
print "Nilai Rata-Rata : %d"%nilai
print "Nilai Huruf     : "

if nilai >= 75 :
    print "A"

elif nilai >= 70 :
    print "B"

elif nilai >= 65 :
    print "C"

elif nilai >= 60 :
    print "D"

if nilai <= 55 :
    print "Keterangan : TIDAK LULUS"
else :
    print "Keterangan : LULUS"
