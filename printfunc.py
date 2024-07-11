
# print string without newline

print('life is')
print('good')

i = ['a','b','c','d','e']

for I in range(5):
    print(i[I])

# in sameline

print('life is', end=" ")
print('good')

i = ['a','b','c','d','e']

for I in range(5):
    print(i[I], end=" ")

# without using forloop

print('life is', end=" ")
print('good')

i = ['a','b','c','d','e']
print(*i)


# not using print func

import sys

sys.stdout.write('life is good ')
sys.stdout.write('when you learn code')
