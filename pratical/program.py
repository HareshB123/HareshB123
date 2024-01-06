import csv
def create():
 f1=open('stud.csv', 'w', newline="")
 writer = csv.writer(f1)
 while True:
     gano=input("Enter Student ID:")
     name=input("Enter Name:")
     place=input("Enter Place:")
     mark=int(input("Enter Mark:"))
     inp=[gano,name,place,mark]
     writer.writerow(inp)
     a=input(("Do you want to continue: (y/n):"))
     if a == 'N' or a == 'n':
         break
         f1.close()
def display_name():
     f1 = open('stud.csv','r')
     rec = csv.reader(f1)
     flag = 0
     print("List of student(s) who scored more than 97 marks:")
     for i in rec:
         if int(i[3])>97:
             print(i[1])
     flag=1
     if flag == 0:
         print("NILL")
     f1.close()
