
# Creates a list of 5 numbers.
a = [1, 2, 3, 4, 5]
print(a)

# Adds a new number to the list.
a.append(6)
print(a)

# Removes the second number from the list.
a.remove(a[1])
print(a)

# Prints the sum of all numbers in the list
ans = 0
for i in a:
    ans += i
print(ans)

#using building functions
ans = sum(a)
print(ans)
