try:
    a = 0
    if(a != 0):
        print("test")
    else:
        raise Exception('hello')
        5/a
except ZeroDivisionError as e:
    print("0�ł͊���Z�ł��܂���")
except Exception as e:
    print(type(e))
    print(e)
    