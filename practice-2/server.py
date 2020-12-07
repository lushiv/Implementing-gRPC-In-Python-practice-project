from concurrent import futures
import grpc
import  users
import login_pb2_grpc
import login_pb2


class UserInfoServicer(login_pb2_grpc.UserAcesssServicer):

    def UserAcesssService(self, request, context):
        id = request.id
        username = request.username
        password = request.password
        response = login_pb2.UserRequest()
        response.username = users.user_info(id=id,username=username,password=password)
        print(response)
        return response
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    login_pb2_grpc.add_UserAcesssServicer_to_server(UserInfoServicer(), server)
    server.add_insecure_port('[::]:50051')
    print('server is running')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()