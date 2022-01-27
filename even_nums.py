import math
anynumber = 8

even_between_one_and_hundered = []
for number in range(1, 101):
    if number % 2 == 0:
        even_between_one_and_hundered.append(number)
print('Even numbers between 1 and 100 are:')
print(even_between_one_and_hundered)

for i in range(1, 13):
    result = i * anynumber
    print(f'{i} x {anynumber} = {result}')

options = input('Enter 1 for dec to bin or 2 for bin to dec: ')
userinput = int(input('Enter a number to convert to binary or decimal: '))
dec = 10
bin = 2
me = []
sum = 0
while userinput > 0 :
    if options == '1':
        rem = userinput % bin
        userinput = int(userinput / 2)
        me.append(rem)
        #print(rem, end="")
    elif options == '2':
        userinput = str(userinput)
        for dig in userinput:
            if len(userinput) > 0:
                power_of_dec = int(len(userinput))
                sum_mult = int(dig) * math.pow(10, power_of_dec )
                sum_of = sum + sum_mult
                power_of_dec = power_of_dec - 1
        print(f'To decimal is: {sum_of}')


me = sorted(me, reverse=True)

for i in me:
    print(i, end="")    