# tìm tất cả các số chia hết cho 7 nhưng không chia hết cho 5
j=[]
for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (",".join(j))