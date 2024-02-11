def pattern(row,column):
  for i in range(1,row+2):
    if i==1:
      for j in range(1,column-1):
        if j<=row:
         print(" ___  ",end="  ")
      print()
    else:  
      for j in range(1,column-1):
        if j<=row: 
          print("/   ",end="")
          print('\\',end="")
          if j!=row:
           print("___",end="")
      print()
      for j in range(1,column-1):
        if j<=row:  
          print("\___/  ", end=" ")
      print()
pattern(int(input("enter the number of rows")),int(input("enter the number of columns")))      
       