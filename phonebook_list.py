i = 0
Name = []
Phone = []
Mail = []
while(True):
    print("""
        Enter -n <name> to enter name
        Enter -p <name> to enter phonenumber beginning with +91
        Enter -e <name> to enter mail ID
        
        P.S.: Enter phone number with at least one other field.    
        """)
    L1 = list(input().split())
    print(L1)
    if(len(L1)<4):
        print("Sorry!! Number of entries insufficient.")# Want to try again? Enter Y or N")
        #ch = input()
    else:
        
        count = 0
        
        if('-p' in L1):
            p = L1.index("-p")
            print("p",p)
            setPhone = set(Phone)
            if (L1[p+1]) not in setPhone:
                s=L1[p+1]
                if(s.startswith('+91')):
                    setPhone.add(L1[p+1])
                    Phone.insert(i,L1[p+1])
                    #print("Phone: ",Phone)
                else: 
                    print("Should begin with +91")
                    #i -= 1
                    continue
            #Phone[i] = ''.join(L1[p+1])
            else:
                print("No dups allowed in phone number")
                #i -= 1
                continue
                
        else:
            print("Entering Phone number was mandatory.")
            #i -= 1
            continue
        
        if('-n' in L1):
            n = L1.index("-n")  
            print("n", n)
            setName = set(Name)
            #if (L1[n+1]) not in setName:
                #setName.add(L1[n+1])
            Name.insert(i,L1[n+1])
            #print("Name: ",Name)
            #Name[i] = ''.join(L1[n+1])
        else:
            count +=1 
            Name[i] = ''  
        
        if('-e' in L1):
            e = L1.index("-e")
            print("e", e)
            setMail = set(Mail)
            if (L1[e+1]) not in setMail:
                setMail.add(L1[e+1])
                Mail.insert(i,L1[e+1])
                #sprint("Mail: i: ",Mail,i)
            #Mail[i] = ''.join(L1[e+1])
            else:
                print("No dups allowed in mail")
                continue
        else:
            count +=1
            Mail[i] = ''
        if(count == 2):
            print("Entering either Name or Mail was mandatory")
            continue
        i +=1
        print("NAME: ", *Name)
        print("Phone: ",*Phone)
        print("Mail: ",*Mail)
        print("Do you want to add more? y or n ")
        if(input() == 'n'):
            exit()
        #print("i: ",i)
print("Program done")
    
        
    
        
    
    
      
    
