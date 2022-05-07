# i=1
# j=1
# while(i<6 and j<25):
#     print(i,j)
#     j=j+i
#     if(i==4 or j==7):
#        continue
#     i=i+1
# print(j)
i=1
j=1
while(i<6):
    print(i,j)
    j=j+i
    if(j!=7):
        j=j+1
    else:
        continue
        i=i+1
    i=i+1
print(j)