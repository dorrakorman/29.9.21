#targil 24 - limzo mehalek meshutaf gadol beyoter shel 2 nums
a = int(input('enter number 1 ='))
b = int(input('enter number 2 ='))
dent = 0

d = 1

if a >= b:
    max_mehalek_num = b
else:
    max_mehalek_num = a
    print ("max_mehalek_num",max_mehalek_num)

while d <= max_mehalek_num + 1:

      if a % d == 0 and b % d == 0:
        dent = d
      d = d + 1

print('dent=',dent)
