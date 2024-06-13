# dekoratory - przyjmuje funkcje jako argument i dodaje do niej nowa funkcjonalnosc
# dekorator wykorzystuje mechniazm funckji zagnizdzonej, wewnetrznej

def decor(func):
    def wew():
        print("Dekorujemy")
        return func()

    return wew

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper

@decor
def hej():

    print("hej")

@uppercase_decorator
def greeting():
    return "Hello World!!"

hej()

print(greeting())
