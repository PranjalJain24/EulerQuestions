if __name__ == '__main__':
    n = 13195 #600851475143
    L = []
    for i in range(2,n):
        if(n % i == 0):
            count = 0
            for j in range(2,i):
                if(i%j != 0):
                    count += 1
            if (count == (i-2)):
                L.append(i)
    print(L[-1])