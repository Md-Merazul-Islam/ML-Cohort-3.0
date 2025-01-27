def summation():
    n=1
    sum = 0; 
    for n in range(100):
        if n%2 == 0:
            sum += n
            continue
    return sum 
add= summation()
print("The summation is: ",add)
আউটপুট: