if __name__ == '__main__':
    n = 0
    L = [0,1]
    while (L[-1] <= 15 ):
        #print(L[-1])
        if (L[-1] % 2 == 0):
            n = n + L[-1]
        L.append(L[-1] + L[-2])
    print(n)