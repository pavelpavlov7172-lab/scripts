def gcd(a,b):
    if a == b :
        return a
    elif a > b:
        return gcd(a-b,b)
    else: #a < b
        return gcd(a,b-a)
def gcd2(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)



if __name__ ==  "__main__" :
    print(gcd(int(input()),int(input())))
    print(gcd2(int(input()),int(input())))