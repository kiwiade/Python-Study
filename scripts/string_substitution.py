a = 'a is {}'.format('test')
print(a)

a = 'a is {} {} {}'.format(1, 2, 3)
print(a)
a = 'a is {0} {1} {2}'.format(1, 2, 3)
print(a)
a = 'a is {2} {1} {0}'.format(1, 2, 3)
print(a)

name = 'My name is {0} {1}. Watashi ha {1} {0}'.format('Jun', 'Sakai')
print(name)
name = 'My name is {name} {family}. Watashi ha {family} {name}'.format(name='Jun', family='Sakai')
print(name)

b = 'apple'
print(f'{b} is red')
x, y, z = 1, 2, 3
print(f'a is {x}, {z}, {y}')
name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. I am {family} {name}')