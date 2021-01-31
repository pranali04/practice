#selection sort
a = [12,77,44,2,0,8]

for i in range(len(a)):
    k = i
    for j in range(i+1,len(a)):
        if a[k]>a[j]:
            k = j
            
    a[i],a[k] = a[k],a[i]

print(a)

#Bubble sort
a = [12,77,44,2,0,8]

for i in range(len(a)):
    swap = False
   
    for j in range(0,(len(a)-i-1)):
       if a[j]>a[j+1]:
           a[j],a[j+1] = a[j+1], a[j]
           swap = True
           
    if swap == False:
        break

print(a)
