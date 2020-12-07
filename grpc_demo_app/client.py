import sys
import grpc
import users_pb2_grpc
import users_pb2
import  logging


def get_users(stub):
    user_id  = int(input('Enter User Id : '))
    username = input('Enter Username : ')
    password = input('Enter Password : ')
    data = users_pb2.UserRequest(user_id=user_id,name=username,password=password)
    response = stub.GetUsers(data)
    print(response.name)


def get_products(stub):
    product_id  = int(input('Enter Product Id : '))
    product_name = input('Enter  Product name : ')
    product_cat = input('Enter product category : ')
    product_des = input('Enter Product Description : ')
    price = int(input('Enter Price : '))

    data = users_pb2.ProductRequest(product_id=product_id,product_name=product_name,product_cat=product_cat,product_des=product_des,price=price)
    response = stub.GetProducts(data)
    print(response.product_name)


def get_vendors(stub):
    vendor_id  = int(input('Enter Vendor Id : '))
    vendor_name = input('Enter Vendor Name : ')
    phone = int(input('Enter Phone : '))
    email = input('Enter Email : ')
    address = input('Enter Address : ')
    data = users_pb2.VendorsRequest(vendor_id=vendor_id,vendor_name=vendor_name,phone=phone,email=email,address=address)
    response = stub.GetVendors(data)
    print(response.vendor_name)


def get_payments(stub):
    payment_id  = int(input('Enter payment Id : '))
    payment_type = input('Enter type : ')
    payment_method = input('Enter Methods : ')
    data = users_pb2.PaymentsRequest(payment_id=payment_id,payment_type=payment_type,payment_method=payment_method)
    response = stub.GetPayments(data)
    print(response.payment_type)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersInfoStub(channel)
        print("-------------- GetUsers Client--------------")
        get_users(stub)
        print("-------------- GetProducts Cleint --------------")
        get_products(stub)
        print("-------------- GetPayments Client --------------")
        get_payments(stub)
        print("-------------- GetVendors Client --------------")
        get_vendors(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()