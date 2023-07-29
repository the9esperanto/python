i = 0
while(i < 10):
    if(i%2 == 0):
        i+=1
        continue
    elif(i == 7):
        i+=1
        break
    else: 
        print(i)
        i+=1