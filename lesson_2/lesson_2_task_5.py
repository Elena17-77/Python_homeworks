def month_to_season(n):
  if n == 1 or n == 2 or n == 12:
   return('зима')
  elif n == 3 or n == 4 or n == 5:
     return('весна')
  elif n == 6 or n == 7 or n == 8:
     return('лето')
  elif n == 9 or n == 10 or n == 11:
     return('осень')
  else: 
    return("Укажите правильный номер месяца")
print(month_to_season(int(input("введите номер месяца"))))