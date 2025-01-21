Rakib = float(input("Enter Rakib CGPA: "))
Tamin = float(input("Enter Tamin CGPA: "))
Meraz = float(input("Enter Meraz CGPA: "))

# lowest cpga 
if Tamin < Rakib and Tamin < Rakib:
    print(f"Tamin's CGPA is the lowest and his CGPA is : ", Tamin)
elif Rakib < Tamin and Rakib < Meraz:
    print(f"Rakib's CGPA is the lowest and his CGPA is : ", Rakib)
else:
    print(f"Meraz's CGPA is the lowest and his CGPA is : ", Meraz)


# average 
avg = (Rakib+ Tamin+Meraz)/3
print(f"The average of the three students' CGPAs is : {avg:0.2f}" )



# output
# Enter Rakib CGPA: 2.64
# Enter Tamin CGPA: 3.58
# Enter Meraz CGPA: 4.00
# Rakib's CGPA is the lowest and his CGPA is :  2.64
# The average of the three students' CGPAs is : 3.41

