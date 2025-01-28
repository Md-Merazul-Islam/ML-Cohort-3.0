strings = "My name  is Md  Merazul  Islam."

while "  " in strings:
    strings = strings.replace('  ',' ')
print(strings)