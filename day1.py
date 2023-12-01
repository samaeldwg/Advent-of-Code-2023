n = [9,8,7,6,5,4,3,2,1]
for i in range(len(n)-1):
    for j in range(len(n)-1):
        if n[j] > n[j+1]: #9 > 8 
            temp = n[j] # 9 
            n[j] = n[j+1]
            n[j+1] = temp 
print(n) 

