# instruckje warunkowe
# instruckje sterwoania przeplywem programu
# if

odp = True
# odp = False

if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza czesc programu")

odp = "Radek"

if odp == "Radek":
    print("To jest Radek")

if odp:
    print("to jest", odp)

if odp == "Tomek":
    print("to jest Tomek")
else:
    print("To nie jest Tomek")

print("Dalsza czesc programu")

podatek = 0
zarobki = int(input("Podaj dochod"))

if zarobki < 10000:
    podatek = 0
elif zarobki <= 29999:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.9

print(f"podatek wynosi {zarobki * podatek}")

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")

rabacik = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabacik}")

# zasymulujemy system zbierania logow
# zmienne beda przechowywac dane , ktore przyszly z innego systemu
# w zaleznosci od danych, bedziemy wykonywac rozne zadania
# email, colnsole, dowolny inny
# dla console alert - komunikat
# "Stalo sie cos strasznego"
# email
# za[isujemy komunikaty do listy
# error, medium, dowolny inny
# dodamy wlasciy opis komunikatu

alert_system = "console"
error = "medium"
error_message = "Stalo sie cos strasznego"
lista_bledow = []

if alert_system == "console":
    print(error_message)
elif alert_system == "email":
    pass  # nic nie rob
    if error == "error":
        lista_bledow.append(error)
        print("wystapil blad error")
    elif error == "medium":
        lista_bledow.append(error)
        print("wystapilo ostrzezenie")
    else:
        print("inny blad")
        lista_bledow.append(error)
else:
    print("inny system")
    print(lista_bledow)

    # test z polskiego
    # pytanie
    # pobierz odpowiedz

odp = input("Jak nazywa sie pierwsza literka z alfabetu")

if odp == "a":
    print("brawo")
else:
    print("nie")
