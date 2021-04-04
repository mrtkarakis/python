import requests

url = "http://data.fixer.io/api/latest?access_key=f91a2d52316c3a8e0c08eac214041bcd"
while True :
    dvz1 = input("çevireceğiniz döviz: ")
    dvz2 = input("çevirilecek döviz: ")
    miktar = float(input("çevirilecek miktarı giriniz: "))

    response = requests.get(url)
    veri = response.json()

    if dvz1 == "EUR":
        print(f"anlık kur üzerinden ({veri['rates'][dvz2]}) {miktar} {dvz1} = {miktar*float(veri['rates'][dvz2])} {dvz2}")
    else:
        rdvz1 = (veri["rates"][dvz2])/(veri["rates"][dvz1])
        print(f"anlık kur üzerinden ({rdvz1}) {miktar} {dvz1} = {miktar * rdvz1} {dvz2}")
