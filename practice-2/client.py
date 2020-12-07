import grpc
import login_pb2_grpc
import login_pb2
from common_utils import  client_conf
import uuid 

from  database.mysql_helper import  DBHelper
db = DBHelper()

def SetUsersData():
    try:    
        with grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),)) as channel:
            stub = login_pb2_grpc.UserAcesssStub(channel)
            # input username info
            id = int(input('Enter User id : '))
            username = input('Enter Your Username : ')
            password = input('Enter Your Password : ') 
            usern_info = login_pb2.UserRequest(id=id,username=username,password=password)
            print('ok')
            response = stub.UserAcesssService(usern_info)
            print(response)
            
            
            
    except Exception as e:
        raise e

SetUsersData()
