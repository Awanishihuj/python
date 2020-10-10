import awanish
choise = int(input('1:jorna\n2: ghatana \n3:bhaga\nEnter the choise => '))
a = int(input('Phela number dale: '))
b = int(input('Dusra number dale: '))
if choise == 1:
    awanish.jorna(a, b)
    print('-'*40)
    print(awanish.jorna.__doc__)
    print('-'*40)
elif choise == 2:
    awanish.ghatana(a , b)
    print('-'*40)
    print(awanish.ghatana.__doc__)
    print('-'*40)
elif choise == 3:
    awanish.bhaga(a , b)
    print('-'*40)
    print(awanish.bhaga.__doc__)
    print('-'*40)
else:
    print('Invalid input')