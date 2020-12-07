import grpc
import usersinfo_pb2_grpc
import usersinfo_pb2


def SetUsersData():
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    # create a stub (client)
    stub = usersinfo_pb2_grpc.UserInfoStub(channel)
    #input data
    user_id  = int(input('Enter User Id : '))
    username = input('Enter Username : ')
    password = input('Enter Password : ')
    # create a valid request message
    data = usersinfo_pb2.UserRequest(user_id=user_id,name=username,password=password)
    # make the call
    response = stub.Username(data)
    # response
    print(response.name)

# SetUsersData()

def SetProductData():
    channel = grpc.insecure_channel('localhost:50051')
    stub = usersinfo_pb2_grpc.ProductInfoStub(channel)
    
    product_id  = int(input('Enter Prouct Id : '))
    product_name = input('Enter Product Name : ')
    product_cat = input('Enter Product Category : ')
    product_des = input('Enter Product Description : ')
    price = int(input("Enter Price : "))

    data = usersinfo_pb2.ProductRequest(product_id=product_id,product_name=product_name,product_cat=product_cat,product_des=product_des,price=price)
    response = stub.Products(data)
    print(response.data)

SetProductData()