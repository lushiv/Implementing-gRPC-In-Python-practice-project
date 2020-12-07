import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='Mobile@97701',
                                    database='python_test',
                                    auth_plugin= 'mysql_native_password')  
        query = 'create table if not exists login_users(userId int primary key,userName varchar(200),user_password varchar(200))'
        cur = self.con.cursor()
        cur.execute(query)
        print('Database connect Sucessfully')


    #Insert
    def insert_user(self, user_id, username, user_password):
        query = "insert into login_users(userId,userName,user_password) values({},'{}','{}')".format(
            user_id, username, user_password)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Your data is saved on db sucessfully")


    #Fech All
    def fetch_all_users(self):
        query = "select * from login_users"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User Name :", row[1])
            print("User Password : ", row[2])
            print()
            print()

    #delete user
    def delete_user(self, userId):
        query = "delete from login_users where userId= {}".format(userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    #update
    def update_user(self, userId, newName, newPassword):
        query = "update login_users set userName='{}',phone='{}' where userId={}".format(
            newName, newPassword, userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")