def spannungsteiler(r1, r2, uges):
    u1 = r1* (uges/(r1 + r2))
    u2 = r2*(uges/(r1 + r2))
    return u2, u1

def stromteiler(rges, r1, r2):

    rges = 1/(1/r1 + 1/r2)
    i1 = iges * (rges / r1)
    i2 = iges * (rges / r2)

l = input("'Spannungsteiler'(1) oder 'Stromteiler'(2)-->")



if l == 1:
    r1 = int(input("bitte r1 in k\u03A9 eingeben-->"))
    r2 = int(input("bitte r2 in k\u03A9 eingeben-->"))
    u = int(input("bitte Uges in V eingeben-->"))
    erg = spannungsteiler(r1, r2, u)

else:
    r1 = int(input("bitte r1 in k\u03A9 eingeben-->"))
    r2 = int(input("bitte r2 in k\u03A9 eingeben-->"))
    erg = stromteiler(rges, r1 ,r2
  

        
    

print("U1={} und U2={}V".format(erg[0],erg[1]))