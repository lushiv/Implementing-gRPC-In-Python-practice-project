import grpc
from concurrent import futures
import time
import logging
import users_pb2_grpc
import  users_pb2
from  methods import  users,products,vendors,payment

class UserInfoService(users_pb2_grpc.UsersInfoServicer):

    def GetUsers(self, request, context):
        response = users_pb2.UserRequest()
        response.name = users.get_users_info(request.user_id,request.name,request.password)
        return response


    def GetProducts(self, request, context):
        response = users_pb2.UserRequest()
        product_id = request.product_id
        product_name = request.product_name
        product_cat = request.product_cat
        product_des = request.product_des
        price = request.price

        response.name = products.get_product_info(product_id,product_name,product_cat,product_des,price)
        return response

    
    def GetPayments(self, request, context):
        response = users_pb2.PaymentsRequest()
        payment_id = request.payment_id
        payment_type = request.payment_type
        payment_method = request.payment_method
        response.payment_type = payment.get_payments_info(payment_id,payment_type,payment_method)
        return response


    def GetVendors(self, request, context):
        response = users_pb2.UserRequest()
        vendor_id = request.vendor_id
        vendor_name = request.vendor_name
        phone = request.phone
        email = request.email
        address = request.address
        response.name = vendors.get_vendors_info(vendor_id,vendor_name,phone,email,address)
        return response
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersInfoServicer_to_server(
        UserInfoService(), server)
    server.add_insecure_port('[::]:50051')
    print('*******************Server is Running on Port : 50051*********************')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
