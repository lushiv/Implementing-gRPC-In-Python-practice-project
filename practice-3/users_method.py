from database.mysql_helper import  DBHelper
db = DBHelper()
import json

def users_info(id,username,password):
  db.insert_user(id, username,password)

  return_data = {'msg': True,'Db status' : 'Sucessfully','User Id' : id,'Username': username, 'password': password}
  
  # convert-dictionary-to-bytes
  user_data = json.dumps(return_data, indent=2).encode('utf-8')
  return user_data



def product_info(product_id,product_name,product_cat,product_des,price):
  return_data = {'msg': True,'product Id' : product_id,'product_name': product_name, 'product_cat': product_cat,'product_des': product_des,'price' : price}
  # convert-dictionary-to-bytes
  product_data = json.dumps(return_data, indent=2).encode('utf-8')
  return product_data
    