nm=[]
n=[]
tgs=[]
uts=[]
uas=[]
stop=False
no=0
while (not stop):
    nama      =raw_input("\tMasukan Nama :")
    nm.append(nama)
    nim       =input    ("\tNIM          :")
    n.append(nama)
    Tugas     =input    ("\tTugas        :")
    tgs.append(Tugas)
    Nilai_UTS =input    ("\tUTS          :")
    uts.append(Nilai_UTS)
    Nilai_UAS =input    ("\tUAS          :")
    uas.append (Nilai_UAS)
    data      =raw_input ("Tambah Data (Y/T)?")
    if (data == 't' ):
        stop = true
        akhir=(Tugas+Nilai_UTS+Nilai_UAS)/3
        no += 1
print "###################################################################################"
print "  No   |    Nama     |    Nim    |    Tugas    |    UTS   |   UAS   |    Akhir     "
print " ",no," |   ",nama,"    |  ",nim,"  |  ",Tugas,"  |  ",Nilai_UTS,"  |  ",Nilai_UAS, "
print "###################################################################################"

