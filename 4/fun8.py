def allparams(a, b, c=42, d=456):
    print(a, b)
    print(c, d)


allparams(1, 2)


def allparams2(a, b, /, c=42, d=456):
    print(a, b)
    print(c, d)


allparams2(6,7)
allparams2(6,7, c=7)

def allparam_3(a,b,/,c=42,*args,d=256,**kwargs):
    print("a,b",a,b)
    print("c,d",c,d)
    print("args", args)
    print("kwargs", kwargs)

allparam_3(1,2)
allparam_3(1,2,3)
allparam_3(1,2,3,4,5,6,d=7, name="radek")
