

def power(a:float,n:int)->int:
    if n==0:
        return 1
    elif n%2==0:
        return power(a**2,n/2)
    else:
        return power(a,n-1)*a
if __name__ ==  "__main__" :
    print(power(int(input()),int(input())))