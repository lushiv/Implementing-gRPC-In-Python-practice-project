import grpc
from concurrent import futures
import time
import usersinfo_pb2
import usersinfo_pb2_grpc
import users_method

class UserInfoService(usersinfo_pb2_grpc.UserInfoServicer):
    def Username(self, request, context):
        response = usersinfo_pb2.UserRequest()
        response.name = users_method.users_info(request.user_id,request.name,request.password)
        return response



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
usersinfo_pb2_grpc.add_UserInfoServicer_to_server(
        UserInfoService(), server)
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)



class ProductInfoService(usersinfo_pb2_grpc.UserInfoServicer):
    def Products(self,request,context):
        response = usersinfo_pb2.ProductRequest()
        id = request.product_id
        name = request.product_name
        cat = request.product_cat
        des = request.product_des
        price = request.price
        response.product_id = users_method.product_info(id,name,cat,des,price)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
usersinfo_pb2_grpc.add_ProductInfoServicer_to_server(
        ProductInfoService(), server)
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)