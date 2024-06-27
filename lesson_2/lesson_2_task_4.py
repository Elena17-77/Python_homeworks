x = int(input())
def fizz_buzz(x):
    for x in range(1, x+1):
     if (x % 3 == 0):
      print('fizz') 
     elif(x % 5 == 0):
       print('buzz')
     elif(x % 3 == 0 and x % 5 == 0):
      print('fizz_buzz')
     else:
       print(x)
n = fizz_buzz(x)      

     
    
     
    

    