muz=10
elma=5
sakız=2
cikolata=4
kahve=30
peynir=45
soda=3
süt=16
su=3
gofret=12



alisveris_tutari=muz+elma+sakız+cikolata+kahve+peynir+soda+süt+su+gofret

print("Alışveriş tutarı {}tl.\n".format(alisveris_tutari))

ödeme=int(input("Ödeme yapacağınız miktarı girin:"))

para_üstü=ödeme- alisveris_tutari

if para_üstü==0:
    print("Aldıklarınız tam tuttu.")
elif para_üstü>0:
    print("para üstünüz {}tl idir.".format(para_üstü))
else:
    print("eksik para verdiniz.")
    