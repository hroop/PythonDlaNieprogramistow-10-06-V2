# zenek mirek franek zadanie zenka mowi mirkowi dolary, franek euro



def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"wymieniam USD {kwota} na {kwota *4.0} pln")

    def eur(kwota=0):
        print(f"wymieniam EUR {kwota} na {kwota *4.3} pln")

    if waluta == "eur":
        return eur
    else:
        return usd

zenek_usd = kantor("usd")
zenek_usd(1000)

mirek_eur = kantor("eur")
mirek_eur(1000)