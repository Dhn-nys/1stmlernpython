# BAB 5 - 5.1 Perintah for Deret
# Dhn-nys
# Date 25 oct 2020

# Start program

posisi=int(input("posisi"))
i=0
b=1
jml=0
for i in range(posisi):
    jml=jml+2*b-1
    b=b+1
print("==========================")
print("Jumlah Deret=" ,jml)
# End program
