import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysqldb.",
  database="acad"
)

print(mydb)

class Question:
    def __init__(self, qno,text):
        self.qno=qno
        self.text=text

    def save(self):
        cur=mydb.cursor()
        cur.execute("insert into question (qno,text) values (%s,%s)",(self.qno,self.text))
        mydb.commit()
        print('saved')

    def show(self):
        cur=mydb.cursor()
        cur.execute("select * from question")
        print(cur.fetchone())



q1=Question(2,"Where is Delhi")
q1.save()
q1.show()

