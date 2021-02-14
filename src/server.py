from functools import reduce
from concurrent import futures
import logging


import grpc

protos, services = grpc.protos_and_services("CalculatorService.proto")


class Calculate(services.calculate):
	def add(self, request, context):
		return protos.Answer(ans=sum(request.data))
	def addtwo(self, request, context):
		return protos.Answer(ans=request.a+request.b)
	def sub(self, request, context):
		return protos.Answer(ans=request.a-request.b)
	def mul(self, request, context):
		return protos.Answer(ans=reduce(lambda x,y : x*y,request.data))
	def multwo(self, request, context):
		return protos.Answer(ans=request.a*request.b)
	def div(self, request, context):
		return protos.Answer(ans=request.a/request.b)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_calculateServicer_to_server(Calculate(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
