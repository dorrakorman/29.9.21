#targil 12 - linzo sum sfarot

 num = int(input('enter num='))
 b = num
 a = num
 c = 0
 while b != 0:
     a = b % 10
     b = b // 10
     c += a
 print(c)