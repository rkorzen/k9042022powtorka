
a = 1

def foo(b): 
    print("a widziane z funkcji: ", a)
    #     global a
    #     a = 10
    print("w funkcji (przestrzen lokalna): ")
    #     print("globals", globals())
    print("locals", locals())


# print("na poziomie modulu - przestrzen globalna")
# print("globals", globals())
# print("locals", locals())

print()
foo(20)
print('a z modulu:', a)
