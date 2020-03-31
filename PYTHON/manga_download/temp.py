a = False
b = False
c = False

if a:
    if b:
        if c:
            print('abc')
        else:
            print('ab')
    else:
        if c:
            print('ac')
        else:
            print('a')
else:
    if b:
        if c:
            print('bc')
        else:
            print('b')
    else:
        print('none')