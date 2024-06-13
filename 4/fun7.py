def connect(**opcje):
    print(opcje)
    connect_param = {
        "host":"127.0.0.1",
        "port": "8080"
    }
    connect_param["pwd"] = opcje
    print(connect_param)

connect(a=6)
connect(a=6, b=8)
connect(a=6, b=8, c=23)
connect(a=6, b=8, c=23, name="Radek")

def all_params(*args, **kwargs):
    print(args, kwargs)

all_params()
all_params(1)
all_params(1,2,3)


