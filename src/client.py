import grpc
import grpc.experimental

import logging

protos = grpc.protos("CalculatorService.proto")
services = grpc.services("CalculatorService.proto")

logging.basicConfig()

response = services.calculate.mul(protos.NumbersList(data=[1,2,3,4]),
                                     'localhost:50051',
                                     insecure=True)
print("Calculate Recieved for mul : [1,2,3,4] : ",response.ans)

response = services.calculate.sub(protos.TwoNumbers(a=1,b=2),
                                     'localhost:50051',
                                     insecure=True)
print("Calculate Recieved for sub : a=1 b=2 : ",response.ans)
