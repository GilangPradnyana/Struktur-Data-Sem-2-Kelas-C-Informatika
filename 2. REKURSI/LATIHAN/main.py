def pangkat2(angka, pangkat):
    if pangkat == 0:
        return 1
    else:
        return angka * pangkat2(angka, pangkat-1)   


print(pangkat2(5, 2))
