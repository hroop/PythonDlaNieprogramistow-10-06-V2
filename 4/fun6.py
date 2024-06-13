#funkcja obliczajaca srednia ocen

def liczby(name=None, *cyfry):
    print(cyfry)
    count = len(cyfry)

    suma = 0
    try:
        for c in cyfry:
            suma+= c
        avg = suma/count
        # print(f"Srednia wynosi {suma/count}")
    except ZeroDivisionError:
        print("dzialanie przez zero")
    except Exception as e:
        print("blad", e)
    else:
        print(f" Uczen {name}, srednia wynosi {avg}")
    finally:
        print("obliczone")

liczby("radek",1,2,3,4,5,6)
liczby()
liczby("Tomek",5,6,5,5,6)
liczby("Magda",1,2,3,6)
liczby("Johnny",1,2,3,6)

