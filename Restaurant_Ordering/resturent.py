# Project on Restaurant Management System
import mysql.connector as driver
import sys
import getpass

def user():
    option = input("You are logged in as customer.Press y to continue....\nTo login as employee press 1, to login as admin press 2: ")
    correct=True
    while(correct):
        if(option=="y" or option=="Y"):
            menu_customer()
        if(option=="1" or option=="2"):
            correct_pass=False
            while(correct_pass==False):
                password = getpass.getpass("Enter the password: ")
                if(option=="1" and password=="emp"):
                    correct_pass=True
                    menu_employee()
                elif(option=="2" and password=="adm"):
                    correct_pass=True
                    menu_admin()
                else:
                    print("Wrong input or password please try again!")
        else:
            option = input("Invalid input. \nYou are logged in as customer.\nPress y to continue....\nTo login as employee press 1, to login as admin press 2:  ")

            
def menu_admin():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print()
        print("........MENU.......")
        print("1. CREATE DATABASE")
        print("2. SHOW DATABASES")
        print("3. CREATE TABLE")
        print("4. SHOW TABLES")
        print("5. INSERT RECORD")
        print("6. UPDATE RECORD")
        print("7. DELETE RECORD")
        print("8. SEARCH RECORD")
        print("9. DISPLAY RECORD")
        print("10. Create Order")
        print()
        choice=int(input("Enter the choice (1-9) : "))
        if(choice==1):
            create_database()
        elif(choice==2):
            show_databases()
        elif(choice==3):
            create_table()
        elif(choice==4):
            show_tables()
        elif(choice==5):
            insert_record()
        elif(choice==6):
            update_record()
        elif(choice==7):
            delete_record()
        elif(choice==8):
            search_record()
        elif(choice==9):    
            display_record_admin()
        elif(choice==10):
            order_food()
        else:
            print("Wrong Choice.")
        loop=input("Do you want more try? Press 'y' to continue: ")
    else:
        sys.exit()
        

def menu_employee():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print()
        print("........MENU.......")
        print("1. SEARCH RECORD")
        print("2. DISPLAY RECORD")
        print("3. Create Order")
        print()
        choice=int(input("Enter the choice (1-2) : "))
        if(choice==1):
            search_record()
        elif(choice==2):    
            display_record()
        elif(choice==3):
            order_food()
        else:
            print("Wrong Choice.")
        loop=input("Do you want more try? Press 'y' to continue: ")
    else:
        sys.exit()

def menu_customer():
    loop='y'
    print("\nHello sir, Please select your order: ")
    while(loop=='y' or loop=='Y'):
        order_food()
        loop=input("Do you want more try? Press 'y' to continue: ")

    else:
        sys.exit()


def create_database():
    con=driver.connect(host='localhost',user='root', passwd='root', charset='utf8')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create database if not exists restaurant')
    print()
    print("Database Created")
    con.close()
    
def show_databases():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show databases')
    for i in cur:
        print(i)
    con.close()
    
def create_table():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create table if not exists food(id integer primary key, foodname varchar(15), mrp float, sold integer)')
    print()
    print("Table Created -> Food")
    cur.execute('DESC food')

    con.close()
    
def show_tables():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show tables')
    for i in cur:
        print(i)
    con.close()

def insert_record():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        ID=int(input("ENTER food ID : "))
        NAME=input("ENTER NAME OF food : ")
        mrp=float(input("ENTER food mrp : "))
        quan_sol=int(input("ENTER quantity sold : "))

        cur.execute("INSERT INTO food(id,foodname,mrp,sold) VALUES({},'{}',{},{})".format(ID,NAME,mrp,quan_sol))
        con.commit()
        print('Record Inserted')
        con.close()
    else:
        print("Error : Not Connected")

def update_record():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    cur=con.cursor()
    d=int(input("Enter food ID for update record : "))
    ID=int(input("ENTER NEW food ID : "))
    name=input("ENTER NEW NAME OF food : ")
    mrp=float(input("ENTER NEW mrp FOR food : "))
    quan_sol=int(input("ENTER NEW quantity sold : "))
    query1="update food set id={}, foodname='{}', mrp={}, sold={} where id={}".format(ID,name,mrp,quan_sol,d)
    cur.execute(query1)
    con.commit()
    print("Record Updated")
    con.close()

def delete_record():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    cur=con.cursor()
    d=int(input("Enter food ID for deleting record : "))
    query1="delete from food where id={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def search_record():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    cur=con.cursor()
    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO SEARCH RECORD: ")
    print("1. ACCORDING TO ID")
    print("2. ACCORDING TO NAME")
    print("3. ACCORDING TO mrp")
    print()
    choice=int(input("ENTER THE CHOICE (1-3) : "))
    if choice==1:
          d=int(input("Enter food ID which you want to search : "))
          query1="select * from food where id={}".format(d)
    elif choice==2:
          name=input("Enter food Name which you want to search : ")
          query1="select * from food where foodname='{}'".format(name)
    elif choice==3:
          price=float(input("Enter food mrp which you want to search : "))
          query1="select * from food where mrp={}".format(price)
    else:
          print("Wrong Choice")
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    for i in rec:
        print(i)
    print("Record Searched")
    con.close()

def display_record():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    if con.is_connected():
        #print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from food')
        rec=cur.fetchall()
        count=cur.rowcount
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------+")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t|  Food ID |   Food Name  |    Mrp    |")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------+")
        for i in rec:
            print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t|{0:^9} | {1:12} | {2:10}|'.format(i[0],i[1],i[2])) 
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------+")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t|     Total no. of items are : ",count,"    |")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t+-------------------------------------+")
        #for i in rec:
        #    print(i)
        con.close()
    else:
        print("Error : Database Connection is not success" )

def display_record_admin():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    if con.is_connected():
        #print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from food')
        rec=cur.fetchall()
        count=cur.rowcount
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------|-----------+")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t|  Food ID |   Food Name  |    Mrp    |    Sold   |")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------|-----------+")
        for i in rec:
            print('\t\t\t\t\t\t\t\t\t\t\t\t\t|{0:^9} | {1:12} | {2:10}| {3:9} |'.format(i[0],i[1],i[2],i[3]))  
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------|-----------+")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t|                  Total no. of records are : ",count," |")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t+-------------------------------------------------+")
        #for i in rec:
        #    print(i)
        con.close()
    else:
        print("Error : Database Connection is not success" )

def order_food():
    con=driver.connect(host='localhost',user='root',passwd='root',charset='utf8',database='restaurant')
    if con.is_connected():
        #print("Successfully Connected")
        cur=con.cursor()
        display_record()
        order = {}
        cur.execute('select * from food')
        bre=cur.fetchall()
        for i in bre:
            order[i[0]] = 0
        print("Please enter the Food ID and quantities of your order: ")
        print("\nTO COMPLETE THE ORDER PLEASE TYPE -> 0")
        while(True):
            f_id = int(input("Enter the Food ID: "))
            if(f_id == 0):
                break
            if(order[f_id] > 0):
                print("THIS ITEM IS ALREADY IN THE CART IF YOU WANT TO MODIFY THE QUANTITY ENTER THE NEW QUANTITY-")
            f_quantity = int(input("Enter Quantity: "))
            print()
            order[f_id] = f_quantity
        final_cost = 0
        print("\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------|-----------|-----------+")
        print("\t\t\t\t\t\t\t\t\t\t\t\t|  Food ID |   Food Name  |    Mrp    |  Quantity |    Cost   |")
        print("\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------|-----------|-----------+")
        for ids in order.keys():
            cur.execute("select * from food where id={}".format(ids))
            rec=cur.fetchall()
            count=cur.rowcount
            for i in rec:
                if(order[ids]>0):
                    total_cost = i[2]*order[ids]
                    final_cost = final_cost + total_cost
                    print('\t\t\t\t\t\t\t\t\t\t\t\t|{0:^9} | {1:12} | {2:10}| {3:9} | {4:9} |'.format(i[0],i[1],i[2],order[ids], total_cost)) 
                    new_sold=order[ids] + int(i[3])
                    cur.execute("update food set sold={} where id={}".format(new_sold,ids))
                    con.commit()
        print("\t\t\t\t\t\t\t\t\t\t\t\t+----------|--------------|-----------|-----------|-----------+")
        print("\t\t\t\t\t\t\t\t\t\t\t\t|                                           Total: ",final_cost,"    |")
        print("\t\t\t\t\t\t\t\t\t\t\t\t+-------------------------------------------------------------+")
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t     THANKYOU! YOUR ORDER HAS BEEN PLACED.\n")
        
        con.close()
    else:
        print("Error : Database Connection is not success" )


user()



