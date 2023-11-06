# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import school_service.school_service_pb2 as school__service__pb2


class SchoolServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_school_info = channel.unary_unary(
                '/school_service.SchoolService/get_school_info',
                request_serializer=school__service__pb2.GetSchoolRequest.SerializeToString,
                response_deserializer=school__service__pb2.GetSchoolResponse.FromString,
                )
        self.get_rp_info = channel.unary_unary(
                '/school_service.SchoolService/get_rp_info',
                request_serializer=school__service__pb2.GetRpRequest.SerializeToString,
                response_deserializer=school__service__pb2.GetRpResponse.FromString,
                )


class SchoolServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_school_info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_rp_info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SchoolServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_school_info': grpc.unary_unary_rpc_method_handler(
                    servicer.get_school_info,
                    request_deserializer=school__service__pb2.GetSchoolRequest.FromString,
                    response_serializer=school__service__pb2.GetSchoolResponse.SerializeToString,
            ),
            'get_rp_info': grpc.unary_unary_rpc_method_handler(
                    servicer.get_rp_info,
                    request_deserializer=school__service__pb2.GetRpRequest.FromString,
                    response_serializer=school__service__pb2.GetRpResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'school_service.SchoolService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SchoolService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_school_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/school_service.SchoolService/get_school_info',
            school__service__pb2.GetSchoolRequest.SerializeToString,
            school__service__pb2.GetSchoolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_rp_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/school_service.SchoolService/get_rp_info',
            school__service__pb2.GetRpRequest.SerializeToString,
            school__service__pb2.GetRpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
