import grpc
import cal_pb2
import cal_pb2_grpc
import  client_conf


def GetSqrRootData():
    try:    
        with grpc.insecure_channel(client_conf.server_address()) as channel:
            stub = cal_pb2_grpc.CalculatorStub(channel)
            store_value = input("Enter Your value:")
            number = cal_pb2.Number(value=int(store_value))
            print(number)
            print(type(number))
            response = stub.SquareRoot(number)
       
    except Exception as e:
        raise e

GetSqrRootData()


