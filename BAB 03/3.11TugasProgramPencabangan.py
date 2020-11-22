# BAB 3

# Start program
QTY=int(input("Banyak Barang ? ")) # Input banyak barang
HRGBRG=int(input("Harga Barang Rp.")) # Input harga barang
JMLBRG=QTY*HRGBRG
if JMLBRG > 300000:
    if HRGBRG > 100000:
        keterangan="Tidak dapat diskon"
    else:
        keterangan="Dapat diskon"
else:
    keterangan="Dapat diskon"
if QTY > 100:
    BYRAKH=JMLBRG-(JMLBRG*0.3)
else:
    BYRAKH=JMLBRG
print("Keterangan : ",keterangan)
print("Total Bayar Akhir Rp.",BYRAKH)
# End Program
