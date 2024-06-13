# funkcja wewnetrzna, zagniezdzona
# dekoratory - uzywaja mechnizmu funkcji wewnetrznej

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun 2")

    return fun2


# nazwa funkcji i nawiazsy
print(fun1)
fun1()
xFun = fun1() #przechowuje adress tego co jest w srodku
print(xFun) #<function fun1.<locals>.fun2 at 0x0000020FC8A098A0>
xFun() #to jest fun2