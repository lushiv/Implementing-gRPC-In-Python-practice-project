from database.mysql_helper import  DBHelper
db = DBHelper()
import json

def user_info(id,username,password):
    db.insert_user(id, username,password)
    message = ({'msg': 'sucess'})
    return_data = json.dumps(message, indent=2).encode('utf-8')
    return return_data
    