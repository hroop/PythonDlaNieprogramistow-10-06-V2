# match case
# dziala od pythona 3.10

lista = []
lang = input("Podaj znany ci jezyk programowania")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append("python")
    case "java":
        lista.append("java")
    case _: #warunek domyslny
        print("nie znaleziono jezyka programowania")

print(lista)