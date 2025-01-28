num=[]

for i in range(8):
    x = int(input(f"Enter the number x{i+1}: "))
    num.append(x)
ans= set(num)
print("The number of unique numbers is: ", ans)
print("The number of unique numbers is: ", len(ans))
