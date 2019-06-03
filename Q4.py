if __name__ == '__main__':
    def check_pal(n):
        m = "".join(reversed(n)) 
        if (m == n):
            return True
    maximum = 0
    for i in range(999):
        for j in range(999):
            if(check_pal(str(i*j))):
                if((i*j) > maximum):
                    maximum = i*j
    print(maximum)