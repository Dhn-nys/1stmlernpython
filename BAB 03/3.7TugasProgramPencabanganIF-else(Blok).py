# BAB 3

# Start program
NAMAPGW=(input("Nama Pegawai ")) # input nama
GAPOK=int(input("Gaji Pokok Rp. ")) # Input gajih pokok
JMLJAMKJ=int(input("Jumlah Jam Kerja ")) # Input jumlah jam kerja
GATOR=GAPOK*JMLJAMKJ # Formulas gaji kotor
if GATOR > 500000: # Formula if
    TAX=GATOR*0.5
    keterangan="Pajak" # Output keterangan
else:
    TAX=0
    keterangan="Tidak Pajak" # Output keterangan
GABER=GATOR-TAX # Formula gaji bersih
print("Gaji Kotor Rp.",GATOR) # Output gaji kotor
print("Pajak Rp.",TAX) # Output pajak
print("Gaji Bersih",GABER) # Output gaji bersih
print("Keterangan",keterangan) # Output keterangan 
# End program