# Extended Euclidean Algorithm Example
# This Python program demonstrates the use of the extended Euclidean algorithm
# to find the greatest common divisor (GCD) of two integers and their Bézout's coefficients.

def quotient(x,y):
    return y//x

def remainder(x,y):
    return y%x

def matrix_product(mx1,mx2):
    mxfinal = [
               [mx1[0][0]*mx2[0][0]+mx1[0][1]*mx2[1][0], mx1[0][0]*mx2[0][1]+mx1[0][1]*mx2[1][1]],
               [mx1[1][0]*mx2[0][0]+mx1[1][1]*mx2[1][0], mx1[1][0]*mx2[0][1]+mx1[1][1]*mx2[1][1]]   
                ]

    return mxfinal

def eucl(a,b):

    M = [
        [1,0],
        [0,1]
        ]
    
    while b != 0:

        q = quotient(a,b) 
        r = remainder(a,b)
        
        M2 = [
        [0,1],
        [1,-q]
        ]

        M = matrix_product(M2,M)
        
        b=a
        a=r

        if a==0:
            break

    g=b
    x = M[0][0]
    y = M[0][1]
    res = [g,x,y]

    return res

while True:

    try:

        a = int(input("Enter the first integer (a): "))
        b = int(input("Enter the second integer (b): "))

        if b<a:
            raise ValueError('b must be greater than a')
        
        gcd = eucl(a,b)

        print(f'GCD({a},{b})={gcd[0]}, Bézout coefficients: {gcd[1]}, {gcd[2]}')
        break

    except ValueError as ve:
        print(ve)