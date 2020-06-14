from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        # インスタンス作成
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        # stubのインスタンス変数にprotobufファイルで定義したSayHelloサービスに、
        # protobudファイルで定義したHelloRequestメッセージを行う
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
