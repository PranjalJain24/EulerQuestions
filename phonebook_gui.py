def printtext():
    global e1
    if(e1.get() == ""):
        string1 = 'aa'
    else: 
        string1 = e1.get() 
    print (string1)
    global e2
    if(e2.get() == ""):
        string2 = 'aa'
    else: 
        string2 = e2.get() 
    print (string2)
    global e3
    if(e3.get() == ""):
        string3 = 'aa'
    else: 
        string3 = e3.get()  
    print (string3)
    enter_excel(string1,string2,string3)
    
def print_data():
    excel_file = pd.ExcelFile('test1.xlsx') 
        
    print(excel_file.sheet_names) 
    print("step1")    
        
    df1 = excel_file.parse('Sheet1',index=False) 
    #df1 = {"a":1, "b":2, "c":3}
    for ind in df1.index: 
        print(df1['Name'][ind], df1['Phone'][ind], df1['Mail'][ind], ind) 
        

    root = Tk()
    L = ['Name', 'Phone', 'Mail']
    
    for i, ind in zip(df1.index,df1.index): #Rows
        for j,c in zip(range(3),L): #Columns
            text_var = StringVar()
            # here we are setting cell text value
            text_var.set('%s' % (df1[c][ind]))
            #s=df1[c][ind]
            b = Entry(root, text=text_var)
            b.grid(row=i+10, column=j)

    mainloop()

    
def enter_excel(n,p,m):
    try:
        s = p
        if s.startswith('+91'):
            print("")
        else:
            getmsg("Number should start with +91")
            exit()
    except Exception:
        getmsg("Entering correct phone number is mandatory")
        exit()
    print("Name: Mail: Phone: ",n,m,p)

    if(n == 'aa' and m == 'aa'):
        getmsg("Entering either name or mail is mandatory")
        exit()
        
    s=str(p)
    print(s,p)
    phonere = re.compile("(0|\+91)?[7-9][0-9]{9}")

    #phonere = re.compile(r"(0/+91)?[7-9][0-9]{9}")m

    #mo2 = phonere.search(args.phone)
    if(( not phonere.match(s)) or (len(p) != 13)):
        print(len(p), not phonere.match(s) )
        getmsg("You did not enter valid number")
        exit()
    if (m != None):   
        emailre = re.compile(r"^.+@[^\.].*\.[a-z]{2,}$") 
        #emailre = re.compile(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        #emailre = re.compile(r"^[a-zA-Z0-9_+&*-]+(?:\\."+ "[a-zA-Z0-9_+&*-]+)*@" +  "(?:[a-zA-Z0-9-]+\\.)+[a-z" +  "A-Z]{2,7}$")
        mo1 = emailre.search(str(m))
        if(mo1 == None):
            getmsg("You did not enter valid mail ID")
            exit()
            
            
    try:
        print("step0")
        #fh = open('test', 'r')
        # Store configuration file values
        #fh.close()   
        
        #print("step1")    

        excel_file = pd.ExcelFile('test1.xlsx') 
        
        #print(excel_file.sheet_names) 
        print("step1")    
        
        df1 = excel_file.parse('Sheet1',index=False) 
        #print(df1) 

        df1 = df1.append({'Name': n, 'Phone':s, 'Mail':m}, ignore_index=True)

        print("Append to df1")
        print(s,p)
        #print(df1)

        if(any(df1['Phone'].duplicated())):
            getmsg("Duplicate phone number not allowed")
        df1 = df1.drop_duplicates('Phone')

        if(any(df1['Mail'].duplicated())):
            getmsg("Duplicate mails not allowed")
        df1 = df1.drop_duplicates('Mail')

        print(df1)
        print("Step2")
        
        df1.fillna(0)

        writer = pd.ExcelWriter('test1.xlsx',  
                        engine ='xlsxwriter') 
        
        df1.to_excel(writer, sheet_name ='Sheet1', index=False) 
        getmsg("Data appended to existing file")

        writer.save() 
        print_data()
        
    except Exception as e:
        # Keep preset values 
            
        #writing in excel
        getmsg("Data added to new file")
        wb = Workbook()
        sheet1 = wb.add_sheet('Sheet1')
        sheet1.write(0,0,'Name')
        sheet1.write(0,1,'Phone')
        sheet1.write(0,2,'Mail')
        sheet1.write(1,0,n)
        sheet1.write(1,1,p)
        sheet1.write(1,2,m)
        wb.save('test1.xlsx')   
        print_data() 
    
def getmsg(s):
    messageVar = Message(root, width=300, text = s) 
    messageVar.config(bg='lightgreen') 
    messageVar.grid(row=6 , column=1) 
    root.mainloop( ) 
    
import tkinter  
from tkinter import *
import pandas as pd
import xlsxwriter
import re
import xlwt
from xlwt import Workbook

root = Tk()
root.title('Phone Book')
root.geometry("500x450")

Label(root, text='Name').grid(row=0) 
Label(root, text='Phone').grid(row=1) 
Label(root, text='Mail').grid(row=2)

e1 = Entry(root)
e1.grid(row=0, column=1) 
#e.pack()
e1.focus_set()
e2 = Entry(root)
e2.grid(row=1, column=1) 
#e.pack()
e2.focus_set()
e3 = Entry(root)
e3.grid(row=2, column=1) 
#e.pack()
e3.focus_set()
# ui = e.get()
# print("Ui= ",ui)
b = Button(root,text='Submit',command=printtext)
b.grid(column=1, row=4)

#b.pack(side='bottom')
root.mainloop()


# #Message
# # main = Tk() 
# # ourMessage ='This is our Message'
# # messageVar = Message(main, text = ourMessage) 
# # messageVar.config(bg='lightgreen') 
# # messageVar.pack( ) 
# # main.mainloop( ) 