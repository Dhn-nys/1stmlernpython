# BAB 3

# Start program
qty=int(input("Banyak barang ")) # Input value Banyak barang
harga=int(input("Harga barang ")) # Input value Harga barang
jumlah=qty*harga # Formula procces value jumlah
if jumlah > 1000000: # IF else 
    diskon=jumlah*0.1 # Output jumlah > 1000000
else :  
    diskon=0 # Output jumlah > 1000000
bayar=jumlah-diskon # Formula 
print("Bayar = Ro.",bayar) # Output bayar
# End program