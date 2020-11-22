# BAB 3

# Start program
NIM=int(input("NIM ")) # Input nim
NAMAMHS=(input("Nama Mahasiswa ")) # Input nama mahasiswa
NILAIPY=int(input("Nilai Python ")) # Input nilai
if NILAIPY >= 80: # Formula If elif
    keterangan="A" # Get keterangan
elif NILAIPY > 70 and NILAIPY <= 80:
    keterangan="B" # Get keterangan
elif NILAIPY > 55 and NILAIPY <= 70:
    keterangan="C" # Get keterangan
elif NILAIPY > 40 and NILAIPY <= 55:
    keterangan="D" # Get keterangan
elif NILAIPY >= 30:
    keterangan="E" # Get keterangan    
else:
    keterangan="GAGAL" # End formula if elif
print("KETERANGAN",keterangan) # Output keterangan
# End program