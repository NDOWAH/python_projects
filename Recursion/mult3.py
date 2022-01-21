#multiples of 3
multiples_3 = [ ]
def mult3(n):
    if n == 0:
        return 3
    else:
        return mult3(n-1) + 3

for i in range(1,10):
    multiples_3.append(str(mult3(i)))

print('The multiples of 3 are: %s' % multiples_3)
