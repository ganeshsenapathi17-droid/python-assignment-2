students={
    501:{
        "Name":"Gani",
        "Age":20,
        "Marks(M1,M2,M3)":(10,10,9),
        "Section":1,
    },
    502:{
        "Name":"Hari",
        "Age":19,
        "Marks(M1,M2,M3)":(9,8,7),
        "Section":3,
    },
    503:{
        "Name":"Pavan",
        "Age":18,
        "Marks(M1,M2,M3)":(10,9,9),
        "Section":4,
    },
    504:{
        "Name":"Ram",
        "Age":17,
        "Marks(M1,M2,M3)":(10,10,10),
        "Section":2,
    }
}
s=set(students.keys())
while True:
    
    menu=int(input("Enter 1 to display registered students\n"" Enter 2 to search student by roll number\n"" Enter 3 to remove a student by roll number\n ""Enter 4 to show class topper\n ""Enter 5 to display unique sections:"))

    if menu==1:
        print(students.items())
    elif menu==2:
        while True:
            try:
                x=int(input("Enter roll number:  "))
                break
            except ValueError:
                print("Enter number only!")
        if x in students:
            print(students.get(x))
        else:
           print("Student has to register")
           y=int(input("Enter 1 to register new student or Enter 2 to go to main menu: "))
           if(y==1):
                new=int(input("Enter roll number of the student: "))
                name=input("Enter student name: ")
                age=int(input("Enter age: "))
                m1=int(input("Enter M1 marks: "))
                m2=int(input("Enter M2 marks"))
                m3=int(input("Enter M3 marks"))
                marks=(m1,m2,m3)
                sec=input("Enter section number:")
                students[new]={
                "Name":name,
                "Age":age ,
                "Marks(M1,M2,M3)":marks,
                "Section":sec
                
                  
        }
        print("Student registration successfull")
        print(students.get(new))
    elif menu==3:
        while True:
            try:
                r=int(input("Enter roll number to remove a student: "))
                break
            except ValueError:
                print("Enter number only!")
        print(students.pop(r),"is removed")
    elif menu==4:
        highest=0
        name=""
        
        for i in students:
            total=sum(students[i]["Marks(M1,M2,M3)"])
            if total>highest:
                highest = total
                name= students[i]["Name"]
        print("Topper:",name)
        print("Total Marks:",highest)
    elif menu==5:
        u=set()
        for k in students:
            u.add(students[k]["Section"])
        print(u)
    else:
        continu