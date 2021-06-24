import mysql.connector

class db_connect:
        global dbcon

        def __init__(self):
            self.dbcon =mysql.connector.connect(host="localhost", user="root", passwd="password", database="learning")
            self.c= self.dbcon.cursor()  # c=cursor object



        def add_student(self, id, name,dept, m1, m2, m3, m4, m5):

                query="insert into student values(%s, %s, %s, %s, %s, %s, %s, %s)"
                tuple=(id, name, dept, m1, m2, m3, m4, m5)
                self.c.execute(query,tuple)
                print("values inserted")


                #def create_table(self, id, name, dept, m1, m2, m3, m4, m5):  # creating a table
                #print("creating table students")
                #query = "create table students(id int primary key auto_increment,name varchar(20) not null,dept varchar(20) not null,m1 int not null,m2 int not null,m3 int not null,m4 int not null,m5 int not null)"
                #tuple = (id, name, dept, m1, m2, m3, m4, m5)
                #self.c.execute((query, tuple))
                #flag=1

        def view_student(self, id):
                try:
                        self.c.execute("select * from student where id = {0}".format(id))
                        result = self.c.fetchone()
                        print(result)
                except Exception as e:
                        print("This id doesn't exist..Please create a record ")

                finally:
                        pass


        def delete_student(self, id):

                self.c.execute("delete from student where id = {0}".format(id))
                print("The student record is deleted from table")

        def update_student(self, id, name,dept, m1, m2, m3, m4, m5):

                query="update student set name={0},dept={1},m1={2},m2={3},m3={4},m4={5},m5={6} where id = {7}".format(name,dept,m1,m2,m3,m4,m5,id)
                self.c.execute(query)
                print("values updated")

        def get_allstudent(self):
                self.c.execute("select * from student")
                result=self.c.fetchall()
                print(result)

        def get_average(self,id):
                self.c.execute("select * from student where id ={0}".format(id))
                res = self.c.fetchall()
                print(res)
                sum=res[0][3]+res[0][4]+res[0][5]+res[0][6]+res[0][7]
                avg=sum//5
                print("The total marks is : {0} and average is :{1} ".format(sum,avg))
                

                if(avg>=90 and avg <=100):
                        print("Grade of student is A")
                elif(avg>=80 and avg<=89):
                        print("Grade of student is B")
                elif(avg>=70 and avg<=79):
                        print("Grade is C")
                elif(avg>=60 and avg<=69):
                        print("Grade is D")
                elif(avg>=50 and avg <=59):
                        print("Grade is E ")
                else:
                        print("The student failed")

cl=db_connect()