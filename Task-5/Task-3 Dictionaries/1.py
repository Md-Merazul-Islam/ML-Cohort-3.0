# Creates a dictionary where keys are subject names (e.g., Math, Science) and values are the marks (e.g., 90, 85).
result = {
    'math': 90,
    'science': 85,
    'history': 80,
    'english': 95,
    'geography': 92
}
print(result)


# Adds a new subject with its mark to the dictionary.
result["social"] = 40
print(result)


# Updates the mark for one subject.
result['english'] = 80
print(result)


# Prints the average marks.
print(sum(result.values())/len(result))

#by looping 
total = 0
for i in result.values():
    total += i

print(total / len(result))
