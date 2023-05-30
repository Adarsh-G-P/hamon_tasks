sum_num = 0
for i in range(3,1000):
    if (i%3==0 or i%5==0):
        sum_num +=i
        
print("sum of all the multiples of 3 or 5 below 1000 is:",sum_num,".")        
