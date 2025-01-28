
def num(n):
    total_sum=0
    for i in range(n):
        x = int(input("Enter the number of x: "))
        total_sum += x
    return total_sum /n 

n = int(input("Enter the number: "))
print("The average num is : ", num(n))