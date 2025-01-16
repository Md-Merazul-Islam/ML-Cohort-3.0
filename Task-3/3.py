a = 2
b = 4
c= ~a 
d= ~b 
print(a, " = ",c)

print(b, " = ",d)


"""
if we represent a on 8 bit binary:

                        a = 00000010
                       ~a = 11111101
                        c = 00000010
                                  +1
                         -----------
                         c= 00000011  // 3 but for 2s complement ans will be  -3

if we represent b on 8 bit binary:

                        b = 00000100
                       ~b = 11111011  
                        d=  00000100
                                  +1
                        -------------
                        d=  00000101    // 5 but for 2s complement ans will be  -5

"""
    


