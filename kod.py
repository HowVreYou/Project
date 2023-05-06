fruits = []

f = input('Напишите свои любимые фрукты (not):')
while f != 'not':
    if f in fruits:
        print('Этот фрукт уже есть в списке')
    else:
       fruits.append(f)
    f = input('Напишите еще любимые фрукты:')
    print(fruits)
    input()


