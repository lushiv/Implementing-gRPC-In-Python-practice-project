import grpc
from concurrent import futures
import time

import cal_pb2
import cal_pb2_grpc
import cal


class CalculatorServicer(cal_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, request, context):
        response = cal_pb2.Number()
        response.value = cal.square_root(request.value)
        return response



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
cal_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)


print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)