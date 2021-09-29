#targil 24 - limzo mehalek meshutaf gadol beyoter

a = int(input('enter number 1 ='))
b = int(input('enter number 2 ='))

while a != b:
    if a > b:
     a = a - b
    else:
        b = b - a
print ("mehalek meshutaf gadol beyoter",a)