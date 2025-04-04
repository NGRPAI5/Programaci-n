euros_500=0
euros_200=0
euros_100=0
euros_50=0
euros_20=0
euros_10=0
euros_5=0
euros_2=0
euros_1=0
monedas_50=0
monedas_20=0
monedas_10=0
monedas_5=0
monedas_2=0
monedas_1=0

partes=[]
dinero=input()

partes=dinero.split()
euros=int(partes[0])
centimos=int(partes[1])

dinero=euros*100+centimos

while dinero>=50000:
    euros_500+=1
    dinero-=50000
while dinero>=20000:
    euros_200+=1
    dinero-=20000
while dinero>=10000:
    euros_100+=1
    dinero-=10000
while dinero>=5000:
    euros_50+=1
    dinero-=5000
while dinero>=2000:
    euros_20+=1
    dinero-=2000
while dinero>=1000:
    euros_10+=1
    dinero-=1000
while dinero>=500:
    euros_5+=1
    dinero-=500
while dinero>=200:
    euros_2+=1
    dinero-=200
while dinero>=100:
    euros_1+=1
    dinero-=100
while dinero>=50:
    monedas_50+=1
    dinero-=50
while dinero>=20:
    monedas_20+=1
    dinero-=20
while dinero>=10:
    monedas_10+=1
    dinero-=10
while dinero>=5:
    monedas_5+=1
    dinero-=5
while dinero>=2:
    monedas_2+=1
    dinero-=2
while dinero>=1:
    monedas_1+=1
    dinero-=1


print(f"Banknotes of 500 euros: {euros_500}")
print(f"Banknotes of 200 euros: {euros_200}")
print(f"Banknotes of 100 euros: {euros_100}")
print(f"Banknotes of 50 euros: {euros_50}")
print(f"Banknotes of 20 euros: {euros_20}")
print(f"Banknotes of 10 euros: {euros_10}")
print(f"Banknotes of 5 euros: {euros_5}")
print(f"Coins of 2 euros: {euros_2}")
print(f"Coins of 1 euro: {euros_1}")
print(f"Coins of 50 cents: {monedas_50}")
print(f"Coins of 20 cents: {monedas_20}")
print(f"Coins of 10 cents: {monedas_10}")
print(f"Coins of 5 cents: {monedas_5}")
print(f"Coins of 2 cents: {monedas_2}")
print(f"Coins of 1 cent: {monedas_1}")
