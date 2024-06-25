def fizz_buzz(n):
    for x in range(1, n+1):
     if (x % 3 == 0):
      print('fizz') 
     elif(x % 5 == 0):
       print('buzz')
     elif(x % 3 == 0 and x % 5 == 0):
      print('fizz_buzz')
     else:
       print(x)
n = fizz_buzz(30)      

     
    
     
    

    