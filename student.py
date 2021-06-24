#from dbconn import *
import connection
from connection import db_connect

class student_details(db_connect):

    global c1
    c1=connection.db_connect()


    def main(self):

        while (True):

            print("""
            Please select an option from menu:
            1.Get the student details
            2.Add a student record
            3.Delete a student record
            4.Get all students record
            5.Get Total,Average and Grade of a student
            6.update a student record
            7.Exit""")

            inp=int(input())


            if (inp==1):
                    id=int(input("enter student id: "))
                    c1.view_student(id)


            elif (inp ==2):

                id=int(input("enter student id: "))
                name=input("enter student name: ")
                dept=input("enter the department: ")
                m1=int(input("Enter mark 1 :"))
                m2=int(input("Enter mark 2: "))
                m3=int(input("Enter mark 3: "))
                m4=int(input("Enter mark 4: "))
                m5=int(input("Enter mark 5 : "))

                c1.add_student(id,name,dept, m1, m2, m3, m4, m5)

            elif(inp==3):
                id=int(input("Enter the student id which you want to delete: "))
                c1.delete_student(id)

            elif(inp==4):
                c1.get_allstudent()

            elif(inp==5):
                id=int(input("plese enter the id of the student whose average and grades you want to view: "))
                c1.get_average(id)

            elif(inp==6):
                id= int(input("Please enter the student id you want to update : "))
                name = input("enter student name: ")
                dept = input("enter the department: ")
                m1 = int(input("Enter mark 1 :"))
                m2 = int(input("Enter mark 2: "))
                m3 = int(input("Enter mark 3: "))
                m4 = int(input("Enter mark 4: "))
                m5 = int(input("Enter mark 5 : "))


            elif(inp==7):
                print("Thank you")
                break



s=student_details()
s.main()
