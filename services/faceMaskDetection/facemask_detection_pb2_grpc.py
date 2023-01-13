# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import facemask_detection_pb2 as facemask__detection__pb2


class DetectionStub(object):
    """The Detection service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getPredictions = channel.unary_unary(
                '/objectDetection.Detection/getPredictions',
                request_serializer=facemask__detection__pb2.RequestBytes.SerializeToString,
                response_deserializer=facemask__detection__pb2.PredictionsList.FromString,
                )


class DetectionServicer(object):
    """The Detection service definition.
    """

    def getPredictions(self, request, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DetectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getPredictions': grpc.unary_unary_rpc_method_handler(
                    servicer.getPredictions,
                    request_deserializer=facemask__detection__pb2.RequestBytes.FromString,
                    response_serializer=facemask__detection__pb2.PredictionsList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'objectDetection.Detection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Detection(object):
    """The Detection service definition.
    """

    @staticmethod
    def getPredictions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/objectDetection.Detection/getPredictions',
            facemask__detection__pb2.RequestBytes.SerializeToString,
            facemask__detection__pb2.PredictionsList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)