if __name__ == '__main__':
    n = 11
    while(True):
        #print("n",n)
        flag = 1
        for i in range(1,11):
            if(n%i != 0):
                flag = 0
        if(flag == 1):
            print((n))
            break
        n += 1