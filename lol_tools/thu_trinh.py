i = 0

for i in range(100):

    if i % 3 == 0 :
        print(" con")
    if i % 5 == 0 :
        print(" heo")    
    if i % 3 == 0 and i % 5 == 0:
        print(" con heo")
    else :
        print(i)        
