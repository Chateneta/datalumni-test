# Your code goes here
import re
for x in range(10,1001):
    xs = str(x)
    if (re.match("[^17]",xs) and re.match(".+4.*",xs)):
        temp=0
        for i in range(len(xs)):
            temp=temp+int(xs[i])
        if(temp<=10 and ( (int(xs[0]) + int(xs[1]) )%2 ==1 ) and ( int(xs[len(xs)-1]) == len(xs)) ):
            mystery_number = x
            print(f'Le nombre mystère est le : {mystery_number}')
  



