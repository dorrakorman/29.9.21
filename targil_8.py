# targil 8 be mavo - limzo num positive lowest

 num = int(input('enter number='))
 a = 0
 b = num
 while b > 0:
     if a != b:
         a = b
     b = int(input('enter number='))
 print(a)