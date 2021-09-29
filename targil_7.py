# targil 7 be mavo - ereh hiuvi gavoa be yoter

 num = int(input('enter number='))
 
 
 b = abs(num)
 a = b // 10
 while a != 0:
     b = a
     a = a // 10
 
 print(b)