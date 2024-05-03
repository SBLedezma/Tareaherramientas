from add import add
from resta import resta
from multiplicacion import multiplicacion
from divicion import divicion
from potencia import potencia
from modulo import modulo
def game():
 score = 0
 while True:
    print('======== Menu ========'
    '\n1. Add'
    '\n2. resta'
    '\n3. multiplicacion'
    '\n4. divicion'
    '\n5. potencia'
    '\n6. modulo'
    '\n0. Exit')
    option = int(input('\nChoice an option: '))
    if option == 0:
        break
    num_1 = int(input('Enter first number: '))
    num_2 = int(input('Enter second number: '))
    answer = int(input('Enter you answer: '))

    if option == 1:
        result = add(num_1, num_2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
            break

    elif option == 2:
        result = resta(num_1, num_2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
            break

    elif option == 3:
        result = multiplicacion(num_1, num_2)
        if result == answer:
            score += 2
            print('Correct!!')
        else:
            print('Incorrect')
            break

    elif option == 4:
        result = divicion(num_1, num_2)
        if result == answer:
            score += 2
            print('Correct!!')
        else:
            print('Incorrect')
            break

    elif option == 5:
        result = potencia(num_1, num_2)
        if result == answer:
            score += 3
            print('Correct!!')
        else:
            print('Incorrect')
            break

    elif option == 6:
        result = modulo(num_1, num_2)
        if result == answer:
            score += 6
            print('Correct!!')
        else:
            print('Incorrect')
            break
 print(f'======== Game Over ========'
       f'\nYou score is {score}'
        '\nKeep going!')
game()