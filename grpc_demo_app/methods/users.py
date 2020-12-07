import json
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__))))
import mysql_helper
import common



def get_users_info(user_id,name,password):
    try:
        data ={
            'User Id' : user_id,
            'User Name' : name,
            'User Password' :password
        }
        return_data = common.convert_dic_to_bytes(data)

        return (return_data)
    except Exception as e:
        raise e
