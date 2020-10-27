def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def isPrimitiveRoot(r, m):
    bools = [False]*m
    for i in range(1,m):
        t = r**i%m
        if t==0 or bools[t]:
            return False
        bools[t] = True;
    return True


if __name__ == "__main__":
    #print(gcd(25725, 2613600))
    for x in [8,7,2,11,3,6]:
        print(isPrimitiveRoot(x, 13))