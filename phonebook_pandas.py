import pandas as pd
import xlsxwriter
import argparse
import re
import xlwt
from xlwt import Workbook

parser= argparse.ArgumentParser()
parser.add_argument('-n','--name', help= "Enter name: ")
parser.add_argument('-p', '--phone',help= "Enter phone number")
parser.add_argument('-e','--mail', help ='Enter mail ID')
args = parser.parse_args()

try:
    s = args.phone
    if s.startswith('+91'):
        print("")
    else:
        print("Number should start with +91")
        exit()
except Exception:
    print("Entering correct phone number is mandatory")
    exit()
print("Name: Mail: Phone: ",args.name,args.mail,args.phone)

if(args.name == None and args.mail == None):
    print("Entering either name or mail is mandatory")
    exit()
    
s=str(args.phone)
print(s,args.phone)
phonere = re.compile("(0|\+91)?[7-9][0-9]{9}")

#phonere = re.compile(r"(0/+91)?[7-9][0-9]{9}")m

#mo2 = phonere.search(args.phone)
if(( not phonere.match(s)) or (len(args.phone) != 13)):
    print(len(args.phone), not phonere.match(s) )
    print("You did not enter valid number")
    exit()
if (args.mail != None):   
    emailre = re.compile(r"^.+@[^\.].*\.[a-z]{2,}$") 
    #emailre = re.compile(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
    #emailre = re.compile(r"^[a-zA-Z0-9_+&*-]+(?:\\."+ "[a-zA-Z0-9_+&*-]+)*@" +  "(?:[a-zA-Z0-9-]+\\.)+[a-z" +  "A-Z]{2,7}$")
    mo1 = emailre.search(str(args.mail))
    if(mo1 == None):
        print("You did not enter valid mail ID")
        exit()
        
        
try:
    print("step0")
    #fh = open('test', 'r')
    # Store configuration file values
    #fh.close()   
    
    #print("step1")    

    excel_file = pd.ExcelFile('test1.xlsx') 
    
    print(excel_file.sheet_names) 
    print("step1")    
    
    df1 = excel_file.parse('Sheet1',index=False) 
    #print(df1) 

    df1 = df1.append({'Name': args.name, 'Phone':s, 'Mail':args.mail}, ignore_index=True)

    print("Append to df1")
    print(s,args.phone)
    #print(df1)

    if(any(df1['Phone'].duplicated())):
        print("Duplicate phone number not allowed")
    df1 = df1.drop_duplicates('Phone')

    if(any(df1['Mail'].duplicated())):
        print("Duplicate mails not allowed")
    df1 = df1.drop_duplicates('Mail')

    print(df1)
    print("Step2")
    
    df1.fillna(0)

    writer = pd.ExcelWriter('test1.xlsx',  
                    engine ='xlsxwriter') 
    
    df1.to_excel(writer, sheet_name ='Sheet1', index=False) 

    writer.save() 
    
except Exception as e:
    # Keep preset values 
        
    #writing in excel
    print("writing")
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet1')
    sheet1.write(0,0,'Name')
    sheet1.write(0,1,'Phone')
    sheet1.write(0,2,'Mail')
    sheet1.write(1,0,args.name)
    sheet1.write(1,1,args.phone)
    sheet1.write(1,2,args.mail)
    wb.save('test1.xlsx')
        









