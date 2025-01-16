# Creates a tuple with the names of 5 cities.
a = ("Dhaka", "Mymensingh", "Rajshahi", "Barishal", "Rangpur")
print(a)

# Prints the third city in the tuple.
print(a[2])

# Converts the tuple into a list, adds a new city, and converts it back to a tuple.
b = list(a)
b.append("Sylhet")
a = tuple(b)

# Prints the modified tuple.
print(a)

