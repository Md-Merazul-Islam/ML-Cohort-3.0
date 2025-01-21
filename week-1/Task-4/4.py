n = int(input("Enter the number of N : "))

for i in range(1,n+1,2):
    for j in range(1,i+2,2):
        print(j, end=" ")
    print()
    
    
# Enter the number of N : 7
# 1 
# 1 3
# 1 3 5
# 1 3 5 7