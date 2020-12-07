from mysql_helper import  DBHelper

def main():
    db = DBHelper()
    while True:
        print("***********WELCOME********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice = int(input())
            if (choice == 1):
                #insert user
                uid = int(input("Enter user id: "))
                username = input("Enter username :")
                password = input("Enter password: ")
                db.insert_user(uid, username, password)
                
            elif choice == 2:
                #display  user
                db.fetch_all()
                pass
            elif choice == 3:
                #delete user
                userid = int(
                    input("enter user id to which you want to delete"))
                db.delete_user(userid)
            elif choice == 4:
                #update user
                uid = int(input("enter id of user : "))
                username = input("new name :")
                new_password = input("new password: ")
                db.update_user(uid, username, new_password)

            elif choice == 5:
                break
            else:
                print("Invalid input ! Try again")

        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")


if __name__ == "__main__":
    main()