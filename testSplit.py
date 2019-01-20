GelenKirpikCumle = " Merhaba "
#İlk Karakter
if ( GelenKirpikCumle[0] == " " ):
    GelenKirpikCumle = GelenKirpikCumle[1:]
#Son Karakter
gkcKS = len(GelenKirpikCumle) - 1
if ( GelenKirpikCumle[gkcKS] == " " ):
    print ( len(GelenKirpikCumle) )
    GelenKirpikCumle = GelenKirpikCumle[:gkcKS]

print ( GelenKirpikCumle )  
print ( len(GelenKirpikCumle) )
