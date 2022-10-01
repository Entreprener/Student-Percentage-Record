import mysql.connector

def connection():
    try:
        u=input("Enter the username on MySQL: ")
        p=input("Enter the password on MySQL: ")
        conn = mysql.connector.connect(host='localhost',user=u, password=p,database="student")
        return conn
    except (Exception, mysql.connector.Error) as error:
        print(error)

def write_record():
    try:
        connect=connection()
        roll=int(input("Enter roll no "))
        name=input("Enter name ")
        per=input("Enter per ")
        cursor=connect.cursor()
        c=(roll,name,per)
        query="INSERT INTO stud(roll,Name,Percentage) VALUES(%s,%s,%s)"
        cursor.execute(query,c)
        connect.commit()
        connect.close()
        print("Record added in file")
        input("Press any key to cont ....")
    except:
        pass
    
def display_all():
    print(40*"=")
    print("\n             Student Records\n")
    print(40*"=")
    try:
        connect=connection()
        cursor=connect.cursor()
        query1='''Select * from stud'''
        cursor.execute(query1)
        result = cursor.fetchall()
        i=0
        w=0
        for i in result:
            w+=1
            print(str(w)+". ""Roll=",i[0]," Name=",i[1]," Per=",i[2],sep=' ')
        connect.close()
        input("Press any key to cont ....")
    except:
        pass
        
def search_roll():
    try:
        print(40*"=")
        print("Record Searching By Roll No")
        print(40*"=")
        n=int(input("Enter roll no search "))
        connect=connection()
        cursor=connect.cursor()
        cursor.execute("select * from stud where roll=%s"%(n,))
        i=cursor.fetchone()
        print(40*"=")
        print("Roll=",i[0]," Name=",i[1]," Per=",i[2],sep=' ')
        connect.close()
        input("Press any key to cont ....")
    except:
        print("Record is not found")
    finally:
        pass
        
def search_name():
    try:
        print(40*"=")
        print("Record Searching By Roll No")
        print(40*"=")
        n=input("Enter name to search ")
        connect=connection()
        cursor=connect.cursor()
        cursor.execute("select * from stud where Name='%s'"%(n,))
        i=cursor.fetchone()
        print(40*"=")
        print("Roll=",i[0]," Name=",i[1]," Per=",i[2],sep=' ')
        connect.close()
        input("Press any key to cont ....")
    except:
        print("Record is not Found ")
    finally:
        pass  

def modify_roll():
    try:
        n=int(input("Enter roll no to modify "))
        z=0
        connect=connection()
        cursor=connect.cursor()
        query1="Select * from stud"
        cursor.execute(query1)
        result =cursor.fetchall()
        i=0
        for i in result:
            if(i[0]==n):
                z=1
                print("record found and details are")
                cursor.execute("select * from stud where roll=%s"%(n,))
                i=cursor.fetchone()
                print(40*"=")
                print("Roll=",i[0]," Name=",i[1]," Per=",i[2],sep=' ')
                print("Enter new data ")
                roll=int(input("Enter new roll no "))
                name=input("Enter new name ")
                per=input("Enter new per ")
                q=(roll,name,per,n)
                query3="update stud set roll=%s,Name=%s,Percentage=%s where roll=%s"
                cursor.execute(query3,q)
                connect.commit()
                print("Record updated")
                connect.close()
        if z==0:
            print("Record not found")
    except:
        pass
    input("Press any key to cont ....")

def delete_roll():
    try:
        n=int(input("Enter roll no to delete "))
        connect=connection()
        print("record to delete found and details are")
        cursor=connect.cursor()
        cursor.execute("select * from stud where roll=%s"%(n,))
        i=cursor.fetchone()
        print(40*"=")
        print("Roll=",i[0]," Name=",i[1]," Per=",i[2],sep=' ')
        cursor.execute("delete from stud where roll=%s"%(n,))
        print(40*"=")
        print("Deleted sucessfull")
        connect.commit()
        connect.close()
        input("Press any key to cont ....")
    except:
        print("Record not Found")
    finally:
        pass
    
##Main##
    
while True:
    print(40*"=")
    print("""            Main Menu
            ---------

           1. Add recod
           2. display all records
           3. search by rollno
           4. search by name
           5. Modify by rollno
           6. delete by rollno
           7. exit
    """)
    print(40*"=")
    ch=int(input("Enter your choice "))
    print(40*"=")
    if(ch==1):
        write_record()
    elif(ch==2):
        display_all()
    elif(ch==3):
        search_roll()
    elif(ch==4):
        search_name()
    elif(ch==5):
        modify_roll()
    elif(ch==6):
        delete_roll()
    elif(ch==7):
        print("End")
        break
    else:
        print("Invalid choice.. ")
