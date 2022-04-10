# jeśli definiuje coś na pozimie modułu to jest to w 
# przestrzeni globalnej

a = "global"
b = 10

def foo():

    pass


# poza funkcja
def outer_function():
    # tu jestem wewnatrz funkcji
    # print(globals())
    # global a 
    # a = 10
    print("funkcja outer widzi a: ", a)
    c = "local?"
    print("lokalne zmienne w outer", locals())
    
    def inner_function():
        nonlocal c
        c = 'from inner'
        print('funkcja inner widzia a: ', a)
        print('funkcja inner widzia c: ', c)
       
        print("inner function locals: ", locals())
        
    inner_function()
    print("c w outer:", c)
    


# poza funkcja
# print(c)

# print(globals())
print()
outer_function()